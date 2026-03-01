"""
Main execution script
=======================
Entry point for the EDA pipeline. Accepts CLI arguments
for flexible, reusable execution.

Usage:
    python src/main.py
    python src/main.py --data data/raw_data.csv
    python src/main.py --data data/raw_data.csv --no-heatmap
"""

import argparse
import sys

from config import DATA_PATH, OUTPUT_DATA_PATH
from logger import setup_logger
from data_loader import load_data
from preprocessing import (
    remove_duplicates,
    check_missing_values,
    fill_missing_values,
    basic_statistics,
)
from visualization import (
    save_numeric_distributions,
    save_correlation_heatmap,
    save_boxplots,
)


def parse_args() -> argparse.Namespace:
    """
    Parses command-line arguments for the EDA pipeline.

    Returns:
        argparse.Namespace: Parsed argument object with attributes:
            - data (str): Path to the input CSV dataset.
            - output (str): Path for the cleaned CSV output.
            - fill_strategy (str): Imputation strategy for missing values.
            - no_heatmap (bool): Flag to skip correlation heatmap.
            - no_boxplots (bool): Flag to skip box plots.
    """
    parser = argparse.ArgumentParser(
        description="🔍 Advanced EDA Pipeline — Mohamed Mostafa",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--data",
        type=str,
        default=DATA_PATH,
        help="Path to the input CSV dataset.",
    )
    parser.add_argument(
        "--output",
        type=str,
        default=OUTPUT_DATA_PATH,
        help="Path to save the cleaned dataset.",
    )
    parser.add_argument(
        "--fill-strategy",
        type=str,
        choices=["mean", "median", "mode"],
        default="mean",
        help="Strategy used to fill numeric missing values.",
    )
    parser.add_argument(
        "--no-heatmap",
        action="store_true",
        help="Skip generating the correlation heatmap.",
    )
    parser.add_argument(
        "--no-boxplots",
        action="store_true",
        help="Skip generating the box plots.",
    )
    return parser.parse_args()


def main() -> None:
    """
    Executes the full EDA pipeline:

    1. Parse CLI arguments
    2. Set up the logger
    3. Load raw data
    4. Remove duplicates
    5. Check & fill missing values
    6. Print statistical summary
    7. Generate and save visualisations
    8. Export cleaned dataset

    Returns:
        None
    """
    args = parse_args()
    logger = setup_logger()

    logger.info("=" * 60)
    logger.info("EDA Pipeline — START")
    logger.info("=" * 60)

    # ── 1. Load ───────────────────────────────────────────────────────────────
    df = load_data(args.data)

    # ── 2. Deduplicate ────────────────────────────────────────────────────────
    df = remove_duplicates(df)

    # ── 3. Missing values ─────────────────────────────────────────────────────
    missing = check_missing_values(df)
    print("\n📋 Missing Values per Column:\n", missing[missing > 0].to_string() or "None")

    df = fill_missing_values(df, strategy=args.fill_strategy)

    # ── 4. Statistics ─────────────────────────────────────────────────────────
    stats = basic_statistics(df)
    print("\n📊 Statistical Summary:\n", stats.to_string())

    # ── 5. Visualisations ─────────────────────────────────────────────────────
    save_numeric_distributions(df)

    if not args.no_heatmap:
        save_correlation_heatmap(df)

    if not args.no_boxplots:
        save_boxplots(df)

    # ── 6. Export ─────────────────────────────────────────────────────────────
    df.to_csv(args.output, index=False)
    logger.info(f"Cleaned dataset saved → {args.output}")

    logger.info("=" * 60)
    logger.info("EDA Pipeline — COMPLETE ✅")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()
