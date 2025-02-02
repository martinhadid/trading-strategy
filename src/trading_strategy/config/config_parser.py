"""Parse TOML config files."""

import tomllib

import dacite

from trading_strategy.config import config_spec


def parse_from_file(config_file: str) -> config_spec.ConfigSpec:
    """Parses configuration parameters from a TOML file.

    Args:
        config_file (str): Path to TOML file.

    Returns:
        config_spec.ConfigSpec: Configuration object.
    """
    with open(config_file, "rb") as f:
        config_dict = tomllib.load(f)
        return dacite.from_dict(data_class=config_spec.ConfigSpec, data=config_dict)
