@echo off
:: ─── run.bat ────────────────────────────────────────────────────────────────
:: Windows batch script to bootstrap the virtual environment and run the pipeline.

echo ============================================================
echo  EDA Project – Setup ^& Run
echo ============================================================

:: 1. Create virtual environment (if not present)
IF NOT EXIST "venv\" (
    echo [SETUP] Creating virtual environment...
    python -m venv venv
)

:: 2. Activate virtual environment
echo [SETUP] Activating virtual environment...
call venv\Scripts\activate.bat

:: 3. Install dependencies
echo [SETUP] Installing requirements...
pip install -r requirements.txt --quiet

:: 4. Run the EDA pipeline
echo [RUN] Starting EDA pipeline...
python src/main.py --data data/raw_data.csv %*

echo ============================================================
echo  Pipeline finished! Check outputs/ for results.
echo ============================================================
