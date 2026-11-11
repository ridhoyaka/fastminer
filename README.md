# Fast Miner

A browser-based, desktop, and command-line tool for **binary classification** of tabular data. Load a CSV, Excel, or JSON file, pick a target column with two classes (for example `true`/`false` or `A`/`B`), and train, compare, evaluate, and use classifiers without writing code. **Works fully offline** - all processing and history stay on your machine.

## Features

- **Web app (recommended, cross-platform):** Runs in your browser at `http://127.0.0.1:5000` with address bar visible, works offline, remembers past analyses.
- Tkinter desktop wizard: load data, explore it, configure training, inspect results, predict.
- CLI for reproducible research workflows.
- Loads `.csv`, `.xlsx`, and `.json` files.
- Automatic preprocessing: missing values, numeric scaling, categorical one-hot encoding, datetime conversion.
- Trains and cross-validates several candidates: dummy baseline, logistic regression, random forest, gradient boosting.
- Optional hyperparameter search and balanced class weights.
- Adjustable probability threshold with metrics.
- Manual single-case prediction form (enter feature values, get a label and confidence).
- Batch prediction from a file, exportable to CSV, Excel, or JSON.
- Saves the complete pipeline and metadata so a model can be reloaded without retraining.
- **Persistent history:** Training runs, inspections, and batch predictions are recorded in a local SQLite database.
- **Storage cleanup:** Delete individual old uploads, models, or reports, or clear everything at once from the Storage page.

## Requirements

- Python 3.10 or newer.
- For the Tkinter desktop app (Linux only): Tkinter is a system package and is not installable with pip.

```bash
sudo apt install python3-tk
```

Tkinter ships with the standard Python installers on Windows and macOS.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Web app (browser-based, offline)
open the directory with terminal first then

```bash
fm web
```

Or:

```bash
fm-web
```

Or:

```bash
python -m dc.web.app
```

The app launches at `http://127.0.0.1:5000` and opens your browser automatically. It works completely offline with no external dependencies. The interface is organized as tabs/pages:

1. **Data** — upload a file, preview rows, see binary target candidates.
2. **Explore** — summary statistics, missing values, and class balance. Inspection reports saved to `reports/`.
3. **Train** — configure test size, folds, seed, metric, candidate models, class weights, and optional search. Training runs in background.
4. **Evaluate** — metrics at selected threshold, evaluate on labeled data.
5. **Predict** — manual single-case prediction form, or batch prediction with CSV download.
6. **Model** — browse and load saved models from `models/`.
7. **History** — view past training runs, inspections, and batch predictions (remembered across sessions).
8. **Storage** — see disk usage and delete old uploads, models, reports, or history. Deleting a file also removes its related history and generated report files.

**Simple, documented paths:**
- `data/uploads/` — uploaded files
- `models/` — saved models (.joblib) with metadata
- `reports/` — prediction outputs and inspection reports (.md/.json)
- `.web_data/history.db` — SQLite database of past analyses

## Desktop app (Tkinter)

```bash
fm-gui
```

or:

```bash
python -m dc.gui.app
```

The app is organized as six tabs:

1. **Data** — open a file, preview rows, choose the target and positive class, optionally exclude columns.
2. **Explore** — summary statistics, missing values, and class balance.
3. **Train** — set test size, folds, seed, metric, candidate models, class weights, and optional search. Training runs in the background.
4. **Evaluate** — metrics at the selected threshold, confusion matrix, and ROC curve. Move the threshold slider to see the trade-off.
5. **Predict** — fill in feature values for a single case, or score a whole batch file and export it.
6. **Model** — save the trained model or reload an existing one.

## Command line

Inspect a dataset and find binary target candidates:

```bash
fm inspect data/sample_binary.csv --target approved
```

Train models and save the best pipeline:

```bash
fm train data/sample_binary.csv \
  --target approved \
  --positive True \
  --output models/approval_model.joblib \
  --cv 5 \
  --balanced
```

Options include `--model logistic --model random_forest`, `--exclude`, `--search`, `--test-size`, `--seed`, and `--scoring`.

Evaluate a saved model on labeled data:

```bash
fm evaluate models/approval_model.joblib data/sample_binary.csv --threshold 0.4
```

Score an unlabeled file:

```bash
fm predict models/approval_model.joblib data/sample_new.csv \
  --output reports/predictions.csv \
  --threshold 0.4
```

Predictions include the label, the positive-class probability, and the threshold used.

## Sample data

- `data/sample_binary.csv` — 240 labeled rows. Features describe a loan applicant; target `approved` is `True` or `False`.
- `data/sample_new.csv` — unlabeled rows for batch prediction.

## How the model is trained

1. Rows with a missing target are dropped.
2. The target must contain exactly two classes; the chosen positive class becomes `1`.
3. Preprocessing is fitted inside each cross-validation fold to avoid leakage.
4. Candidate models are compared with stratified cross-validation using the selected metric.
5. The best pipeline is evaluated on a held-out, stratified test set.
6. The full pipeline (preprocessing + model) and metadata are saved so predictions use identical preprocessing.

## Output files

- `models/*.joblib` — trained pipeline.
- `models/*.json` — metadata: target, classes, features, metrics, leaderboard, versions.
- `reports/*.md` and `reports/*.json` — inspection reports.
- Prediction files — CSV, Excel, or JSON.
- `.web_data/history.db` — web app history (SQLite).

## Development

```bash
pip install -e ".[dev]"
pytest
ruff check .
```

## Notes and limitations

- Binary classification only; a target with more or fewer than two classes is rejected with a clear message.
- Very small datasets, heavy class imbalance, or high-cardinality text columns can reduce accuracy. The app warns about imbalance and lets you enable balanced class weights.
- ID-like columns are flagged during inspection but not dropped automatically; exclude them on the Data tab or with `--exclude`.
- Saved models are only guaranteed to load with compatible scikit-learn versions (recorded in the metadata).
