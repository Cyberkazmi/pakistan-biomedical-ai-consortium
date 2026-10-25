"""Load 4D (T, Z, Y, X) microscopy volumes."""
from pathlib import Path
import numpy as np


def load_movie(path: str) -> np.ndarray:
    p = Path(path)
    if p.suffix in {".tif", ".tiff"}:
        import tifffile
        arr = tifffile.imread(p)
    else:
        import zarr
        z = zarr.open(str(p), mode="r")
        arr = z["0"][:] if hasattr(z, "keys") and "0" in z else z[:]
    arr = np.asarray(arr)
    if arr.ndim == 3:  # single timepoint
        arr = arr[None]
    if arr.ndim != 4:
        raise ValueError(f"expected (T,Z,Y,X), got shape {arr.shape}")
    return arr
