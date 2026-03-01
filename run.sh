#!/usr/bin/env bash
# ─── run.sh ─────────────────────────────────────────────────────────────────
# Mac/Linux script to bootstrap the virtual environment and run the pipeline.

set -e

echo "============================================================"
echo " EDA Project – Setup & Run"
echo "============================================================"

# 1. Create virtual environment (if not present)
if [ ! -d "venv" ]; then
    echo "[SETUP] Creating virtual environment..."
    python3 -m venv venv
fi

# 2. Activate virtual environment
echo "[SETUP] Activating virtual environment..."
source venv/bin/activate

# 3. Install dependencies
echo "[SETUP] Installing requirements..."
pip install -r requirements.txt --quiet

# 4. Run the EDA pipeline (forward any extra args: e.g. --no-heatmap)
echo "[RUN] Starting EDA pipeline..."
python src/main.py --data data/raw_data.csv "$@"

echo "============================================================"
echo " Pipeline finished! Check outputs/ for results."
echo "============================================================"
