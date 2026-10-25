# PBAC Pipeline (Phase 0)

Scan → Track → Analyze → Predict, on 3D+time microscopy.

```bash
pip install -r requirements.txt
python run.py --input movie.zarr --out results/ --diameter 8
```

Input: a 4D array (T, Z, Y, X) in OME-Zarr or TIFF.
Output: `masks.zarr`, `tracks_nodes.csv`, `tracks_edges.csv`, `features.parquet`, `forecast.csv`.

First target: the Biohub "Cell Tracking During Development" CC0 dataset (Kaggle). Run on a Kaggle GPU notebook.

Status: scaffold. Segmentation and tracking use published tools (Cellpose, Ultrack); the forecaster is a deliberately simple baseline to beat.
