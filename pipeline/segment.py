"""3D per-timepoint cell segmentation with Cellpose."""
import numpy as np


def segment_movie(movie: np.ndarray, diameter: float = 8.0, gpu: bool = True,
                  model_type: str = "nuclei") -> tuple[np.ndarray, np.ndarray]:
    """Return (labels, cellprob) arrays shaped like movie.

    labels: integer instance masks per timepoint.
    cellprob: foreground probability, used by Ultrack as detection map.
    """
    from cellpose import models
    model = models.CellposeModel(gpu=gpu, model_type=model_type)
    labels = np.zeros(movie.shape, dtype=np.uint32)
    prob = np.zeros(movie.shape, dtype=np.float32)
    for t in range(movie.shape[0]):
        masks, flows, _ = model.eval(movie[t], diameter=diameter, do_3D=True,
                                     channels=[0, 0])
        labels[t] = masks
        prob[t] = 1.0 / (1.0 + np.exp(-flows[2]))  # cellprob logits -> [0,1]
    return labels, prob
