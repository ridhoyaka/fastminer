from __future__ import annotations

import numpy as np
import pandas as pd
from pandas.api import types as ptypes
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer, OneHotEncoder, StandardScaler


def convert_datetimes(frame: pd.DataFrame) -> pd.DataFrame:
    if not isinstance(frame, pd.DataFrame):
        return frame
    result = frame.copy()
    for column in result.columns:
        if ptypes.is_datetime64_any_dtype(result[column]):
            result[column] = result[column].map(
                lambda value: value.timestamp() if pd.notna(value) else np.nan
            )
    return result


def numeric_columns(frame: pd.DataFrame) -> list[str]:
    return [
        str(column)
        for column in frame.columns
        if ptypes.is_numeric_dtype(frame[column]) and not ptypes.is_bool_dtype(frame[column])
    ]


def categorical_columns(frame: pd.DataFrame) -> list[str]:
    numeric = set(numeric_columns(frame))
    return [str(column) for column in frame.columns if str(column) not in numeric]


def build_preprocessor() -> ColumnTransformer:
    numeric_pipeline = Pipeline(
        [
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ]
    )
    categorical_pipeline = Pipeline(
        [
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
        ]
    )
    return ColumnTransformer(
        [
            ("numeric", numeric_pipeline, numeric_columns),
            ("categorical", categorical_pipeline, categorical_columns),
        ],
        remainder="drop",
        verbose_feature_names_out=False,
    )


def build_pipeline(model) -> Pipeline:
    return Pipeline(
        [
            ("datetimes", FunctionTransformer(convert_datetimes)),
            ("preprocess", build_preprocessor()),
            ("model", model),
        ]
    )


def feature_names(pipeline: Pipeline) -> list[str]:
    preprocess = pipeline.named_steps["preprocess"]
    try:
        return [str(name) for name in preprocess.get_feature_names_out()]
    except Exception:
        return []
