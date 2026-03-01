# 📊 Advanced EDA Project

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-4C72B0)
![Status](https://img.shields.io/badge/Project-Production%20Ready-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)

> A production-grade **Exploratory Data Analysis** pipeline with modular architecture,
> professional logging, config management, CLI argument parsing, and automated visualizations.

---

## 📁 Project Structure

```
eda-project/
│
├── data/
│   └── raw_data.csv           ← Input dataset
│
├── src/
│   ├── config.py              ← Centralized configuration
│   ├── logger.py              ← Dual-handler logging system
│   ├── data_loader.py         ← CSV loading with error handling
│   ├── preprocessing.py       ← Deduplication, missing values, stats
│   ├── visualization.py       ← Distribution plots, heatmap, boxplots
│   └── main.py                ← CLI entry point & pipeline orchestrator
│
├── outputs/
│   ├── figures/               ← Auto-generated plots (PNG)
│   ├── cleaned_data.csv       ← Cleaned dataset export
│   └── project.log            ← Full execution log
│
├── requirements.txt
├── .gitignore
├── run.bat                    ← One-click run (Windows)
├── run.sh                     ← One-click run (Mac/Linux)
└── README.md
```

---

## 🚀 Features

| Feature | Description |
|---|---|
| 🗂️ Modular Architecture | Each concern lives in its own focused module |
| 📝 Logging System | File + console dual-handler with timestamps |
| ⚙️ Config Management | Single `config.py` controls all paths & settings |
| 🖥️ CLI Execution | `argparse` for flexible, scriptable runs |
| 🔄 Auto Preprocessing | Deduplication, missing-value imputation |
| 📈 Auto Visualizations | Distributions, correlation heatmap, box plots |
| 💾 Dataset Export | Cleaned CSV output at end of pipeline |
| 📚 Full Docstrings | Every function documented with params & returns |

---

## ⚙️ Setup

### 1. Clone the repository
```bash
git clone https://github.com/YourUsername/eda-project.git
cd eda-project
```

### 2. Create and activate Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Pipeline

### Quick run (uses defaults from `config.py`)
```bash
python src/main.py
```

### Custom dataset path
```bash
python src/main.py --data data/raw_data.csv
```

### All available flags
```bash
python src/main.py --help
```

```
usage: main.py [-h] [--data DATA] [--output OUTPUT]
               [--fill-strategy {mean,median,mode}]
               [--no-heatmap] [--no-boxplots]

🔍 Advanced EDA Pipeline — Mohamed Mostafa

options:
  --data            Path to input CSV dataset     (default: data/raw_data.csv)
  --output          Path to save cleaned dataset  (default: outputs/cleaned_data.csv)
  --fill-strategy   Missing-value imputation      (default: mean)
  --no-heatmap      Skip correlation heatmap
  --no-boxplots     Skip box plots
```

### One-click scripts

**Windows:**
```bat
run.bat
```

**Mac / Linux:**
```bash
chmod +x run.sh && ./run.sh
```

---

## 📈 Outputs

After a successful run you will find:

| Output | Location |
|---|---|
| Cleaned dataset | `outputs/cleaned_data.csv` |
| Execution log | `outputs/project.log` |
| Distribution plots | `outputs/figures/<col>_distribution.png` |
| Correlation heatmap | `outputs/figures/correlation_heatmap.png` |
| Box plots | `outputs/figures/boxplots.png` |

---

## 🧱 Module Overview

### `config.py`
Centralised configuration — edit this file to change paths, log level, and plot settings without touching business logic.

### `logger.py`
Sets up a named logger with two handlers: a **FileHandler** (persistent log) and a **StreamHandler** (real-time console output).

### `data_loader.py`
Reads any CSV with `pd.read_csv` and raises descriptive, typed exceptions (`FileNotFoundError`, `ParserError`) instead of bare `Exception`.

### `preprocessing.py`
- `remove_duplicates()` — drops exact duplicate rows with a before/after count.
- `check_missing_values()` — returns a `pd.Series` of null counts per column.
- `fill_missing_values()` — imputes numeric nulls with mean / median / mode.
- `basic_statistics()` — returns `df.describe(include='all')`.

### `visualization.py`
- `save_numeric_distributions()` — one histogram+KDE per numeric column.
- `save_correlation_heatmap()` — annotated heatmap for all numeric columns.
- `save_boxplots()` — side-by-side box plots for outlier detection.

---

## 👨‍💻 Author

**Mohamed Mostafa**  
Data Science & AI Enthusiast

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute.
