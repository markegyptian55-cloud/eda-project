"""
Data preprocessing module
===========================
Provides functions for cleaning, inspecting, and
summarising a Pandas DataFrame before analysis.
"""

import logging
import pandas as pd

logger = logging.getLogger("eda_logger")


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Removes exact duplicate rows from the dataset.

    Parameters:
        df (pd.DataFrame): Input dataframe.

    Returns:
        pd.DataFrame: Dataframe with duplicates removed.

    Example:
        >>> df_clean = remove_duplicates(df)
    """
    before = df.shape[0]
    df = df.drop_duplicates()
    after = df.shape[0]
    removed = before - after
    if removed > 0:
        logger.info(f"Removed {removed} duplicate row(s).")
    else:
        logger.info("No duplicate rows found.")
    return df


def check_missing_values(df: pd.DataFrame) -> pd.Series:
    """
    Returns the count of missing values per column.

    Parameters:
        df (pd.DataFrame): Input dataframe.

    Returns:
        pd.Series: Missing value counts indexed by column name.

    Example:
        >>> missing = check_missing_values(df)
        >>> print(missing[missing > 0])
    """
    missing = df.isnull().sum()
    total_missing = missing.sum()
    logger.info(
        f"Missing value check complete — total missing cells: {total_missing}."
    )
    return missing


def fill_missing_values(df: pd.DataFrame, strategy: str = "mean") -> pd.DataFrame:
    """
    Fills missing values in numeric columns using the chosen strategy.

    Parameters:
        df (pd.DataFrame): Input dataframe.
        strategy (str): Imputation strategy — 'mean', 'median', or 'mode'.
                        Defaults to 'mean'.

    Returns:
        pd.DataFrame: Dataframe with missing values filled.

    Raises:
        ValueError: If an unsupported strategy is provided.

    Example:
        >>> df_filled = fill_missing_values(df, strategy="median")
    """
    numeric_cols = df.select_dtypes(include="number").columns
    valid_strategies = {"mean", "median", "mode"}

    if strategy not in valid_strategies:
        raise ValueError(
            f"Unsupported strategy '{strategy}'. Choose from {valid_strategies}."
        )

    for col in numeric_cols:
        if df[col].isnull().any():
            if strategy == "mean":
                fill_val = df[col].mean()
            elif strategy == "median":
                fill_val = df[col].median()
            else:
                fill_val = df[col].mode()[0]
            df[col] = df[col].fillna(fill_val)
            logger.info(f"Filled missing values in '{col}' using {strategy}.")

    return df


def basic_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Returns a statistical summary (describe) of the dataset.

    Parameters:
        df (pd.DataFrame): Input dataframe.

    Returns:
        pd.DataFrame: Descriptive statistics (count, mean, std, min, quartiles, max).

    Example:
        >>> stats = basic_statistics(df)
        >>> print(stats)
    """
    logger.info("Generated statistical summary.")
    return df.describe(include="all")
