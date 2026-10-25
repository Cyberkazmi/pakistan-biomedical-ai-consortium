"""Per-cell, per-timepoint features (shape, intensity/refractive index, motion)."""
import numpy as np
import pandas as pd
from skimage.measure import regionprops_table


PROPS = ("label", "area", "centroid", "intensity_mean", "intensity_max",
         "extent", "solidity", "axis_major_length", "axis_minor_length")


def extract_features(labels: np.ndarray, movie: np.ndarray) -> pd.DataFrame:
    rows = []
    for t in range(labels.shape[0]):
        tbl = regionprops_table(labels[t], intensity_image=movie[t], properties=PROPS)
        df = pd.DataFrame(tbl)
        df["t"] = t
        rows.append(df)
    feats = pd.concat(rows, ignore_index=True).rename(columns={
        "centroid-0": "z", "centroid-1": "y", "centroid-2": "x", "area": "volume"})
    feats["elongation"] = feats["axis_major_length"] / feats["axis_minor_length"].clip(lower=1e-6)
    return feats


def add_motion(feats: pd.DataFrame, nodes: pd.DataFrame) -> pd.DataFrame:
    """Attach track ids and per-step speed by nearest centroid match."""
    from scipy.spatial import cKDTree
    out = []
    for t, f in feats.groupby("t"):
        n = nodes[nodes.t == t]
        if n.empty:
            continue
        d, i = cKDTree(n[["z", "y", "x"]].values).query(f[["z", "y", "x"]].values)
        f = f.copy()
        f["track_id"] = n.iloc[i]["track_id"].values
        out.append(f)
    df = pd.concat(out).sort_values(["track_id", "t"])
    step = df.groupby("track_id")[["z", "y", "x"]].diff()
    df["speed"] = np.sqrt((step ** 2).sum(axis=1))
    return df
