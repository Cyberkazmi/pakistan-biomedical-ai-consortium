"""PBAC Phase 0 end-to-end: segment -> track -> features -> forecast."""
import argparse
from pathlib import Path

from io_utils import load_movie
from segment import segment_movie
from track import track_movie, to_nodes_edges
from features import extract_features, add_motion
from forecast import label_divisions, train_and_score


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--out", default="results")
    ap.add_argument("--diameter", type=float, default=8.0)
    ap.add_argument("--cpu", action="store_true")
    a = ap.parse_args()
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)

    movie = load_movie(a.input)
    print("movie", movie.shape)
    labels, _ = segment_movie(movie, diameter=a.diameter, gpu=not a.cpu)
    tracks_df, _ = track_movie(labels, workdir=str(out / "ultrack"))
    nodes, edges = to_nodes_edges(tracks_df)
    nodes.to_csv(out / "tracks_nodes.csv", index=False)
    edges.to_csv(out / "tracks_edges.csv", index=False)

    feats = add_motion(extract_features(labels, movie), nodes)
    feats = label_divisions(feats, edges, nodes)
    feats.to_parquet(out / "features.parquet")
    if feats["divides_soon"].nunique() > 1:
        _, scores, pred = train_and_score(feats)
        pred.to_csv(out / "forecast.csv", index=False)
        print(f"division forecast ROC-AUC (5-fold, by track): {scores.mean():.3f} ± {scores.std():.3f}")
    print("done ->", out)


if __name__ == "__main__":
    main()
