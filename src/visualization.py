"""
Visualization module
======================
Generates and saves EDA plots using Matplotlib and Seaborn.
All figures are persisted to FIGURES_PATH defined in config.py.
"""

import logging
import os

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from config import FIGURES_PATH, FIGURE_DPI, FIGURE_STYLE

logger = logging.getLogger("eda_logger")

# Apply global seaborn style once at import time
sns.set_style(FIGURE_STYLE)


def _ensure_output_dir() -> None:
    """Creates the figures output directory if it does not already exist."""
    os.makedirs(FIGURES_PATH, exist_ok=True)


def save_numeric_distributions(df: pd.DataFrame) -> None:
    """
    Saves histogram + KDE distribution plots for all numeric columns.

    Each column gets its own PNG file saved to FIGURES_PATH.

    Parameters:
        df (pd.DataFrame): Input dataframe to visualise.

    Returns:
        None

    Example:
        >>> save_numeric_distributions(df)
    """
    _ensure_output_dir()
    numeric_cols = df.select_dtypes(include="number").columns

    if len(numeric_cols) == 0:
        logger.warning("No numeric columns found — skipping distribution plots.")
        return

    for col in numeric_cols:
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.histplot(df[col].dropna(), kde=True, ax=ax, color="#4C72B0")
        ax.set_title(f"Distribution of {col}", fontsize=14, fontweight="bold")
        ax.set_xlabel(col)
        ax.set_ylabel("Frequency")
        plt.tight_layout()
        out_path = os.path.join(FIGURES_PATH, f"{col}_distribution.png")
        fig.savefig(out_path, dpi=FIGURE_DPI)
        plt.close(fig)
        logger.info(f"Saved distribution plot → {out_path}")

    logger.info(f"All {len(numeric_cols)} distribution plot(s) saved.")


def save_correlation_heatmap(df: pd.DataFrame) -> None:
    """
    Saves a correlation heatmap for numeric columns to FIGURES_PATH.

    Parameters:
        df (pd.DataFrame): Input dataframe.

    Returns:
        None

    Example:
        >>> save_correlation_heatmap(df)
    """
    _ensure_output_dir()
    numeric_df = df.select_dtypes(include="number")

    if numeric_df.shape[1] < 2:
        logger.warning("Need at least 2 numeric columns for a correlation heatmap.")
        return

    fig, ax = plt.subplots(figsize=(10, 8))
    corr = numeric_df.corr()
    sns.heatmap(
        corr,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        linewidths=0.5,
        ax=ax,
    )
    ax.set_title("Correlation Heatmap", fontsize=15, fontweight="bold")
    plt.tight_layout()
    out_path = os.path.join(FIGURES_PATH, "correlation_heatmap.png")
    fig.savefig(out_path, dpi=FIGURE_DPI)
    plt.close(fig)
    logger.info(f"Saved correlation heatmap → {out_path}")


def save_boxplots(df: pd.DataFrame) -> None:
    """
    Saves box plots for all numeric columns to detect outliers.

    Parameters:
        df (pd.DataFrame): Input dataframe.

    Returns:
        None

    Example:
        >>> save_boxplots(df)
    """
    _ensure_output_dir()
    numeric_cols = df.select_dtypes(include="number").columns

    if len(numeric_cols) == 0:
        logger.warning("No numeric columns found — skipping box plots.")
        return

    fig, ax = plt.subplots(
        1, len(numeric_cols), figsize=(5 * len(numeric_cols), 5), squeeze=False
    )
    for i, col in enumerate(numeric_cols):
        sns.boxplot(y=df[col].dropna(), ax=ax[0][i], color="#55A868")
        ax[0][i].set_title(col, fontsize=12, fontweight="bold")

    plt.tight_layout()
    out_path = os.path.join(FIGURES_PATH, "boxplots.png")
    fig.savefig(out_path, dpi=FIGURE_DPI)
    plt.close(fig)
    logger.info(f"Saved box plots → {out_path}")
