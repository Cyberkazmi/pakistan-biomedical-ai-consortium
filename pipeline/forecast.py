"""Baseline forecaster: will this cell divide within the next k frames?

Deliberately simple (gradient boosting on recent features) so that later
models have a clear baseline to beat.
"""
import pandas as pd
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.model_selection import GroupKFold, cross_val_score

FEATURES = ["volume", "intensity_mean", "elongation", "solidity", "speed"]


def label_divisions(df: pd.DataFrame, edges: pd.DataFrame, nodes: pd.DataFrame, k: int = 5) -> pd.DataFrame:
    out_deg = edges.groupby("source_id").size()
    dividing_nodes = out_deg[out_deg >= 2].index
    div = nodes[nodes.node_id.isin(dividing_nodes)][["track_id", "t"]].rename(columns={"t": "t_div"})
    df = df.merge(div, on="track_id", how="left")
    df["divides_soon"] = ((df["t_div"] - df["t"]).between(0, k)).astype(int)
    return df.drop(columns="t_div")


def train_and_score(df: pd.DataFrame):
    data = df.dropna(subset=FEATURES)
    X, y, groups = data[FEATURES], data["divides_soon"], data["track_id"]
    model = HistGradientBoostingClassifier(max_iter=200)
    scores = cross_val_score(model, X, y, groups=groups, cv=GroupKFold(5), scoring="roc_auc")
    model.fit(X, y)
    data = data.assign(p_divide=model.predict_proba(X)[:, 1])
    return model, scores, data[["track_id", "t", "p_divide"]]
