import logging
import colorlog
from logging.handlers import RotatingFileHandler
import os

logging.basicConfig(
    level=os.getenv("LOG_LEVEL", logging.DEBUG),  # Log all messages DEBUG and above
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  # Log message format
)


def setup_logger(name: str) -> logging.Logger:
    """Setup logger to handle logs with formating and log leverl control"""

    logger = logging.getLogger(name)
    level = os.getenv("LOG_LEVEL", "DEBUG").upper()
    logger.setLevel(level)

    color_formatter = colorlog.ColoredFormatter(
        "%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        log_colors={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "bold_red",
        },
    )
    handler = RotatingFileHandler("app.log", maxBytes=1e6, backupCount=5)
    handler.setLevel(level)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    handler.setFormatter(color_formatter)
    console_handler.setFormatter(color_formatter)

    logger.addHandler(handler)
    logger.addHandler(console_handler)

    return logger
