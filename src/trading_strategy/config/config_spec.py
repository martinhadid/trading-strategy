"""App and library configuration spec."""

import dataclasses
import json


@dataclasses.dataclass
class DataConfigSpec:
    """Data-level configuration spec.

    Attributes:
        period (int): amount of data to download.
    """

    period: str = "5y"


@dataclasses.dataclass
class PlotsConfigSpec:
    """Data-level configuration spec.

    Attributes:
        x_rotation (int): x-axis rotation.
        value_offset (int): distance from the plot.
        fig_size (tuple[int, int]): figure size.
        arrow_size (int): arrow size.


    """

    x_rotation: int = 90
    value_offset: list[int] | tuple[int, int] = (5, 25)
    fig_size: list[int] | tuple[int, int] = (25, 3)
    arrow_size: int = 150

    def __post_init__(self):
        """Post initialization routine."""
        self.value_offset = tuple(self.value_offset)
        self.fig_size = tuple(self.fig_size)


@dataclasses.dataclass
class ProjectConfigSpec:
    """Project-level configuration spec.

    Attributes:
        stop_loss (int): Stop loss percentage for the trading strategy.
    """

    stop_loss: float = 0.06


@dataclasses.dataclass
class RSIConfigSpec:
    """RSI configuration spec.

    Attributes:
        period (int): amount of days to consider.
    """

    period: int = 14


@dataclasses.dataclass
class StochasticOscillatorConfigSpec:
    """Stochastic oscillator configuration spec.

    Attributes:
        d_time_periods (int): amount of days to consider.
        k_slowing_periods (int): slowing periods.
        k_time_periods (int): time periods.
    """

    d_time_periods: int = 3
    k_slowing_periods: int = 6
    k_time_periods: int = 14


@dataclasses.dataclass
class OptimizationsConfigSpec:
    """Optimizations-level configuration spec.

    Attributes:
        rsi_period (int): amount of days to consider.
    """

    rsi: RSIConfigSpec
    stochastic_oscillator: StochasticOscillatorConfigSpec


@dataclasses.dataclass
class ConfigSpec:
    """Overall configuration spec."""

    project: ProjectConfigSpec
    data: DataConfigSpec
    plots: PlotsConfigSpec
    optimizations: OptimizationsConfigSpec

    def to_json(self) -> str:
        """Returns JSON representation of the configuration."""
        return json.dumps(dataclasses.asdict(self), indent=4)
