"""Link segmented cells across time with Ultrack; export Biohub-style nodes/edges."""
import numpy as np
import pandas as pd


def track_movie(labels: np.ndarray, workdir: str = "ultrack_work"):
    from ultrack import MainConfig, track, to_tracks_layer
    from ultrack.utils import labels_to_contours

    detection, contours = labels_to_contours(labels, sigma=1.0)
    cfg = MainConfig()
    cfg.data_config.working_dir = workdir
    cfg.segmentation_config.min_area = 20
    cfg.linking_config.max_distance = 15.0
    track(cfg, detection=detection, edges=contours, overwrite=True)
    tracks_df, graph = to_tracks_layer(cfg)
    return tracks_df, graph


def to_nodes_edges(tracks_df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Convert Ultrack tracks table to node and edge tables."""
    df = tracks_df.reset_index(drop=True).copy()
    df["node_id"] = np.arange(len(df))
    nodes = df[["node_id", "track_id", "t", "z", "y", "x"]]
    key = df.set_index(["track_id", "t"])["node_id"]
    edges = []
    for (tid, t), nid in key.items():
        nxt = key.get((tid, t + 1))
        if nxt is not None:
            edges.append((nid, nxt))
    # division edges: parent track's last node -> first node of each child track
    parents = df.groupby("track_id")["parent_track_id"].first()
    first = df.sort_values("t").groupby("track_id")["node_id"].first()
    last = df.sort_values("t").groupby("track_id")["node_id"].last()
    for child, parent in parents.items():
        if parent is not None and parent >= 0 and parent in last.index:
            edges.append((last[parent], first[child]))
    return nodes, pd.DataFrame(edges, columns=["source_id", "target_id"])
