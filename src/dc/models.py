from __future__ import annotations

from sklearn.dummy import DummyClassifier
from sklearn.ensemble import HistGradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression

MODEL_LABELS = {
    "dummy": "Dummy baseline",
    "logistic": "Logistic regression",
    "random_forest": "Random forest",
    "hist_gradient_boosting": "Gradient boosting",
}


def build_candidate_models(
    seed: int = 42,
    class_weight: str | None = None,
) -> dict[str, object]:
    weight = class_weight or None
    return {
        "dummy": DummyClassifier(strategy="prior"),
        "logistic": LogisticRegression(max_iter=2000, class_weight=weight),
        "random_forest": RandomForestClassifier(
            n_estimators=300,
            min_samples_leaf=2,
            class_weight=weight,
            random_state=seed,
            n_jobs=-1,
        ),
        "hist_gradient_boosting": HistGradientBoostingClassifier(
            random_state=seed,
            class_weight=weight,
        ),
    }


def search_spaces() -> dict[str, dict[str, list]]:
    return {
        "logistic": {
            "model__C": [0.01, 0.1, 1.0, 10.0],
            "model__solver": ["lbfgs", "liblinear"],
        },
        "random_forest": {
            "model__n_estimators": [200, 400, 600],
            "model__max_depth": [None, 4, 8, 16],
            "model__min_samples_leaf": [1, 2, 5],
        },
        "hist_gradient_boosting": {
            "model__learning_rate": [0.03, 0.06, 0.1, 0.2],
            "model__max_iter": [150, 300, 500],
            "model__max_leaf_nodes": [15, 31, 63],
        },
        "dummy": {},
    }
