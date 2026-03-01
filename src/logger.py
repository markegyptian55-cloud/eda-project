"""
Logger configuration module
=============================
Sets up a unified logging system that writes to both
a log file and the console simultaneously.
"""

import logging
import os
import sys
from config import LOG_FILE, LOG_LEVEL


def setup_logger(name: str = "eda_logger") -> logging.Logger:
    """
    Configures and returns a logger instance.

    Sets up dual-handler logging:
      - FileHandler  → writes structured logs to LOG_FILE
      - StreamHandler → prints colour-friendly logs to stdout

    Parameters:
        name (str): Logger name identifier. Defaults to 'eda_logger'.

    Returns:
        logging.Logger: Configured logger instance ready to use.
    """
    # Ensure output directory exists before creating the log file
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

    logger = logging.getLogger(name)

    # Avoid adding duplicate handlers on repeated calls
    if logger.handlers:
        return logger

    logger.setLevel(getattr(logging, LOG_LEVEL, logging.INFO))

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # ── File handler ──────────────────────────────────────────────────────────
    file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    file_handler.setFormatter(formatter)

    # ── Console handler ───────────────────────────────────────────────────────
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
