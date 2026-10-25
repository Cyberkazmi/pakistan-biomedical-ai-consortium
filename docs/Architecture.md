# PBAC Architecture

Version 0.2 · Draft

## Layers

```
[Imaging]  holotomography / QPI  ·  light-sheet  ·  public datasets (Biohub CC0)
     │
[Data Agent]       ingest (zarr/tiff) → QC → metadata → versioned storage
     │
[Tracking Agent]   segmentation (Cellpose / micro-SAM) → linking (Ultrack / Trackastra) → lineage graph
     │
[Analysis Agent]   per-cell features: volume, shape, refractive index, motion, division timing
     │
[Prediction Agent] models on feature time-series → fate / viability / response forecasts
     │
[Validation Agent] metrics vs ground truth, cross-model agreement, flags for human review
     │
[Action Agent]     advisory report for researcher/clinician (never autonomous treatment)
```

## Principles
- Open, reproducible code; pinned environments; every result regenerable from raw data.
- Human-in-the-loop: specialist sign-off before any clinical interpretation.
- Patient data: consented, de-identified, access-controlled; never committed to this repository.
- Compute: Kaggle/Colab for Phase 0; HPC partner for 4D training at scale.

## Data formats
- Images: OME-Zarr. Tracks: nodes/edges CSV (Biohub format) + GEFF/tracksdata where possible.
- Features: Parquet, one row per cell per timepoint.

## Code layout
```
pipeline/
  segment.py    # Cellpose / micro-SAM wrapper
  track.py      # Ultrack linking + lineage
  features.py   # per-cell feature extraction
  forecast.py   # baseline fate/division forecaster
  run.py        # end-to-end CLI
```
