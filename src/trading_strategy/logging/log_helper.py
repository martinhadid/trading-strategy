"""Helper routines for logging."""

import enum
import json
import logging
import pathlib
import sys

from trading_strategy.datetime import datetime_helper

BASE_LOG_DIR = pathlib.Path("logs")


class LogColors(enum.StrEnum):
    """Enum for log colors."""

    DEBUG = "\033[36m"  # Cyan
    INFO = "\033[32m"  # Green
    WARNING = "\033[33m"  # Yellow
    ERROR = "\033[31m"  # Red
    CRITICAL = "\033[31;1m"  # Bold Red
    RESET = "\033[0m"
    TIMESTAMP = "\033[37m"  # Light Gray
    FILENAME = "\033[35m"  # Purple


class StdoutFormatter(logging.Formatter):
    """Formatter for stdout with colors."""

    def format(self, record):
        """Format the specified record as text."""
        timestamp = self.formatTime(record, "%Y-%m-%d %H:%M:%S")
        file_line_no = f"{record.filename}:{record.lineno}"
        return f"""
            {LogColors[record.levelname].value}[{record.levelname}]
            {LogColors.TIMESTAMP.value}{timestamp}{LogColors.RESET.value}
            {LogColors.FILENAME.value}{file_line_no}{LogColors.RESET.value} -
            {record.getMessage()}
        """


class FileFormatter(logging.Formatter):
    """Formatter for log file in JSON format."""

    def format(self, record):
        """Format the specified record as text."""
        log_record = {
            "timestamp": self.formatTime(record, "%Y-%m-%d %H:%M:%S"),
            "level": record.levelname,
            "filename": record.filename,
            "lineno": record.lineno,
            "message": record.getMessage(),
        }
        return json.dumps(log_record)


def get_log_file_path(
    *, name: str, label: str | None = None, log_dir: pathlib.Path = BASE_LOG_DIR
) -> pathlib.Path:
    """Returns a log file path.

    Args:
        name (str): Base name of the log file to use. This should typically be
            the name of the main Python script to be logged.
        label (str | None): Optional suffix to append to the log file name.
            Name format: {name}-{label}
        log_dir (pathlib.Path): Log directory where log file should be placed;
            otherwise defaults to `_BASE_LOG_DIR`.

    Returns:
        pathlib.Path: Path to the log file.
    """
    log_dir.mkdir(parents=True, exist_ok=True)
    file_prefix = name.rsplit(".", 1)[-1]
    file_suffix = f"-{label}" if label else ""
    return (
        log_dir
        / f"{file_prefix}-{datetime_helper.get_datetime_string()}{file_suffix}.log"
    )


def create_log_handlers(log_file: str | None = None) -> list[logging.Handler]:
    """Creates log handlers.

    This creates the following log handlers:
    - StreamHandler that prints colorized messages to STDOUT
    - FileHandler that logs messages to a file in JSON format.

    Args:
        log_file (str | None): Optional file where logs will be written to as JSON.

    Returns:
        list[logging.Handler]: List of log handlers that were created.
    """
    # Add STDOUT handler
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(StdoutFormatter())
    handlers = [stdout_handler]
    # Add log file handler with JSON formatting
    if log_file is not None:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(FileFormatter())
        handlers.append(file_handler)

    return handlers


def configure_basic_logging(
    log_level: str = "INFO", log_file: pathlib.Path | None = None
):
    """Configures logging for all loggers."""
    logging.basicConfig(level=log_level, handlers=create_log_handlers(log_file))
    logging.info("Logging level set to %s", log_level)
    if log_file:
        logging.info("Writing logs to file: %s", log_file)
