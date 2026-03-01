"""
Data loading module
=====================
Handles reading datasets from disk with proper
error handling and logging.
"""

import logging
import pandas as pd

logger = logging.getLogger("eda_logger")


def load_data(path: str) -> pd.DataFrame:
    """
    Loads a dataset from a given CSV file path.

    Parameters:
        path (str): Relative or absolute path to the CSV file.

    Returns:
        pd.DataFrame: Loaded dataset as a Pandas DataFrame.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        pd.errors.ParserError: If the file cannot be parsed as CSV.
        Exception: Re-raises any other unexpected error after logging it.

    Example:
        >>> df = load_data("data/raw_data.csv")
        >>> print(df.shape)
    """
    logger.info(f"Loading dataset from: {path}")
    try:
        df = pd.read_csv(path)
        logger.info(
            f"Dataset loaded successfully — shape: {df.shape[0]} rows × {df.shape[1]} cols."
        )
        return df
    except FileNotFoundError:
        logger.error(f"File not found: '{path}'. Check the DATA_PATH in config.py.")
        raise
    except pd.errors.ParserError as parse_err:
        logger.error(f"CSV parsing error: {parse_err}")
        raise
    except Exception as exc:
        logger.error(f"Unexpected error loading dataset: {exc}")
        raise
