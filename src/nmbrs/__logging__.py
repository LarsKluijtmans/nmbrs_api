"""Logging instance initializer"""

import logging
from logging.config import dictConfig


def logger_config(logging_level=logging.WARNING):
    """
    Initialize logging configuration.

    Args:
        logging_level (int, optional): Logging level to be set. Defaults to logging.INFO.
    """
    # Define logging configuration dictionary
    logging_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {"verbose": {"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"}},
        "handlers": {
            "console": {
                "level": logging_level,
                "class": "logging.StreamHandler",
                "formatter": "verbose",
            }
        },
        "loggers": {
            "nmbrs": {
                "level": logging_level,
                "propagate": True,
                "handlers": ["console"],
            }
        },
    }

    dictConfig(logging_config)


logger_config()
