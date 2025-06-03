"""Helper routines for date and time operations."""

from datetime import datetime


def get_datetime_string() -> str:
    """Returns a current date time in YYYY-MM-DD-HHMMSS format."""
    return datetime.now().strftime("%Y%m%d-%H%M%S")
