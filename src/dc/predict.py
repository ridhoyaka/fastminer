from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
from pandas.api import types as ptypes

from dc.io import load_dataframe, save_dataframe
from dc.train import load_bundle


def _positive_probability(pipeline, frame: pd.DataFrame) -> np.ndarray:
    probabilities = pipeline.predict_proba(frame)
    classes = list(pipeline.classes_)
    if 1 not in classes:
        raise ValueError("Loaded model does not contain a positive (1) class.")
    return probabilities[:, classes.index(1)]


def _coerce_frame(bundle: dict[str, Any], frame: pd.DataFrame) -> pd.DataFrame:
    dtypes = bundle.get("metadata", {}).get("feature_dtypes", {})
    result = frame.copy()
    for column, dtype in dtypes.items():
        if column not in result.columns:
            continue
        try:
            if dtype in ("bool", "boolean"):
                result[column] = result[column].map(_coerce_bool).astype("boolean")
            elif dtype.startswith("datetime"):
                result[column] = pd.to_datetime(result[column], errors="coerce")
            elif _is_numeric_dtype(dtype):
                result[column] = pd.to_numeric(result[column], errors="coerce")
            else:
                values = result[column].astype("object")
                result[column] = values.where(values.map(lambda v: not _blank(v)), np.nan)
        except (TypeError, ValueError):
            continue
    return result


def _is_numeric_dtype(dtype: str) -> bool:
    try:
        return ptypes.is_numeric_dtype(np.dtype(dtype))
    except TypeError:
        return False


def _blank(value: Any) -> bool:
    return isinstance(value, str) and value.strip() == ""


def _coerce_bool(value: Any) -> Any:
    if isinstance(value, (bool, np.bool_)):
        return bool(value)
    if value is None or (isinstance(value, float) and np.isnan(value)):
        return pd.NA
    text = str(value).strip().lower()
    if text in {"true", "1", "yes", "y", "positive"}:
        return True
    if text in {"false", "0", "no", "n", "negative"}:
        return False
    return pd.NA


def required_features(bundle: dict[str, Any]) -> list[str]:
    features = bundle.get("metadata", {}).get("feature_columns")
    if not features:
        raise ValueError("Model metadata is missing the list of feature columns.")
    return list(features)


def predict_probabilities(bundle: dict[str, Any], frame: pd.DataFrame) -> np.ndarray:
    features = required_features(bundle)
    missing = [column for column in features if column not in frame.columns]
    if missing:
        raise ValueError(f"Input data is missing required column(s): {', '.join(missing)}")
    features_frame = _coerce_frame(bundle, frame[features])
    return _positive_probability(bundle["pipeline"], features_frame)


def predict_frame(
    bundle: dict[str, Any],
    frame: pd.DataFrame,
    threshold: float | None = None,
) -> pd.DataFrame:
    metadata = bundle.get("metadata", {})
    chosen_threshold = float(metadata.get("threshold", 0.5) if threshold is None else threshold)
    if not 0.0 <= chosen_threshold <= 1.0:
        raise ValueError("Threshold must be between 0 and 1.")

    probabilities = predict_probabilities(bundle, frame)
    positive_label = metadata.get("positive_label", 1)
    negative_label = metadata.get("negative_label", 0)
    predictions = np.where(probabilities >= chosen_threshold, positive_label, negative_label)

    output = frame.copy()
    output["prediction"] = predictions
    output[f"probability_{positive_label}"] = np.round(probabilities, 6)
    output["threshold"] = chosen_threshold
    return output


def predict_record(
    bundle: dict[str, Any],
    record: dict[str, Any],
    threshold: float | None = None,
) -> dict[str, Any]:
    frame = pd.DataFrame([record])
    result = predict_frame(bundle, frame, threshold=threshold)
    row = result.iloc[0]
    probability_column = next(
        column for column in result.columns if str(column).startswith("probability_")
    )
    return {
        "prediction": row["prediction"].item()
        if hasattr(row["prediction"], "item")
        else row["prediction"],
        "probability": float(row[probability_column]),
        "threshold": float(row["threshold"]),
        "positive_label": bundle.get("metadata", {}).get("positive_label", 1),
        "negative_label": bundle.get("metadata", {}).get("negative_label", 0),
    }


def predict_file(
    model_path: str | Path,
    input_path: str | Path,
    output_path: str | Path,
    threshold: float | None = None,
) -> tuple[pd.DataFrame, Path]:
    bundle = load_bundle(model_path)
    frame = load_dataframe(input_path)
    result = predict_frame(bundle, frame, threshold=threshold)
    saved = save_dataframe(result, output_path)
    return result, saved
