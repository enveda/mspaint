import logging
from textwrap import dedent
from typing import Literal, Tuple

import holoviews as hv
import numpy as np
import pandas as pd

from mspaint.functions import setup_plot_data

# set up a logger
logger = logging.getLogger(__name__)


# define a plotter class that initializes with a plotting engine
# defined by the user
class Plotter:
    ENGINES = ("bokeh", "matplotlib", "plotly")

    def __init__(self, plotting_engine: Literal[ENGINES]):
        self.plotting_engine = plotting_engine
        if self.check_valid_plotting_engine():
            self.set_plotting_engine()
        else:
            raise ValueError(
                dedent(
                    f"Plotting engine {self.plotting_engine} is not valid. "
                    f"Please choose from: {self.ENGINES}"
                )
            )

    def set_plotting_engine(self):
        if self.get_plotting_engine() == "plotly":
            hv.extension(self.plotting_engine, logo=False, inline=False)
        else:
            hv.extension(self.plotting_engine, logo=False)
        logger.info(f"Plotting engine set to {self.plotting_engine}")

    def get_plotting_engine(self):
        return self.plotting_engine

    def check_valid_plotting_engine(self):
        return self.plotting_engine in ["bokeh", "matplotlib", "plotly"]

    def make_mirror_plot(
        self,
        mzs_on_bottom: np.array,
        intensities_on_bottom: np.array,
        mzs_on_top: np.array,
        intensities_on_top: np.array,
        label_top: str = "top",
        label_bottom: str = "bottom",
        title: str = "title",
    ):
        # setup plot data i.e. normalize intensities, calculate x axis range,
        # and make gapped arrays
        (
            mzs_on_bottom,
            intensities_on_bottom,
            mzs_on_top,
            intensities_on_top,
            xaxis_range,
        ) = setup_plot_data(
            mzs_on_bottom, intensities_on_bottom, mzs_on_top, intensities_on_top
        )

        plot = (
            hv.Curve(
                (mzs_on_top, intensities_on_top), "m/z", "intensity", label=label_top
            )
            * hv.Curve(
                (mzs_on_bottom, intensities_on_bottom),
                "m/z",
                "intensity",
                label=label_bottom,
            ).opts(title=title, xlim=xaxis_range)
        )

        if self.get_plotting_engine() == "plotly":
            plot *= hv.HLine(0)
        else:
            plot *= hv.HLine(0).opts(color="black")

        return plot

    def check_mz_range_width(self, mz_range: Tuple[float, float]):
        # check if range is too wide and warn user
        if mz_range[1] - mz_range[0] > 0.01:
            logger.warning(
                dedent(
                    f"\nmz_range is very wide. We recommend using a range < 0.01 Da. \
                Using given range {mz_range} to make plot."
                )
            )

    def check_mz_range_and_value(
        self, mz_range: Tuple[float, float], mz_value: float, mz_tolerance: float
    ) -> Tuple[float, float]:
        if mz_range is None:
            if mz_value is None:  # both none, raise exception
                raise ValueError(
                    dedent(
                        """\nBoth mz_range and mz_value are None. \
                            Please provide one or the other."""
                    )
                )
            else:  # range none, value given, use it
                mz_range = (mz_value - mz_tolerance, mz_value + mz_tolerance)
        if mz_range is not None and mz_value is not None:  # if both are given
            logger.warning(
                dedent(
                    f"""\nBoth mz_range and mz_value were given. \
                        Using mz_range {mz_range} to make plot."""
                )
            )
        return mz_range

    def check_aggregated_dataframe(self, aggregated_dataframe, mz_range):
        if aggregated_dataframe.empty:
            raise ValueError(
                dedent(
                    f"""\nNo data found in mz_range {mz_range}. \
                        Please check your mz_range."""
                )
            )

    def aggregated_plot_setup(
        self,
        dataframe,
        intensity_column: str,
        rt_column: str,
        mz_range: Tuple[float, float] = None,
        mz_column: str = None,
        aggregation_function: str = "sum",
    ):
        if mz_range is not None:  # mz range given, filter to it
            dataframe = dataframe.loc[
                dataframe[mz_column].between(mz_range[0], mz_range[1])
            ]
        agg = dataframe.groupby(rt_column).agg({intensity_column: aggregation_function})
        self.check_aggregated_dataframe(aggregated_dataframe=agg, mz_range=mz_range)
        return agg

    def make_xic_plot(
        self,
        xic_dataframe: pd.DataFrame,
        mz_range: Tuple[float, float] = None,
        mz_value: float = None,
        mz_tolerance: float = 0.005,
        rt_column: str = "rt",
        intensity_column: str = "intensity",
        mz_column: str = "mz",
    ):
        mz_range = self.check_mz_range_and_value(mz_range, mz_value, mz_tolerance)
        self.check_mz_range_width(mz_range)

        agg = self.aggregated_plot_setup(
            dataframe=xic_dataframe,
            mz_range=mz_range,
            mz_column=mz_column,
            intensity_column=intensity_column,
            rt_column=rt_column,
            aggregation_function="sum",
        )

        # plot figure
        return hv.Curve((agg.index, agg[intensity_column]), "rt", "intensity").opts(
            title=f"XIC for m/z=[{mz_range[0]}, {mz_range[1]}]"
        )

    def make_tic_plot(
        self,
        tic_dataframe: pd.DataFrame,
        rt_column: str = "rt",
        intensity_column: str = "intensity",
    ):
        agg = self.aggregated_plot_setup(
            dataframe=tic_dataframe,
            intensity_column=intensity_column,
            rt_column=rt_column,
            aggregation_function="sum",
        )

        # plot figure
        return hv.Curve((agg.index, agg[intensity_column]), "rt", "intensity").opts(
            title="TIC"
        )

    def make_bpc_plot(
        self,
        bpc_dataframe: pd.DataFrame,
        rt_column: str = "rt",
        intensity_column: str = "intensity",
    ):
        agg = self.aggregated_plot_setup(
            dataframe=bpc_dataframe,
            intensity_column=intensity_column,
            rt_column=rt_column,
            aggregation_function="max",
        )

        # plot figure
        return hv.Curve((agg.index, agg[intensity_column]), "rt", "intensity").opts(
            title="BPC"
        )

    def make_2d_plot(
        self,
        dataframe: pd.DataFrame,
        x_axis: str = "rt",
        y_axis: str = "mz",
        color_axis: str = "intensity",
        cmap: str = "viridis",
        alpha: float = 0.1,
    ):
        # plot figure
        return hv.Points(
            data=dataframe.sort_values(color_axis),
            kdims=[x_axis, y_axis],
            vdims=[color_axis],
        ).opts(color=color_axis, cmap=cmap, alpha=alpha)

    def make_3d_plot(
        self,
        dataframe: pd.DataFrame,
        x_axis: str = "rt",
        y_axis: str = "mz",
        z_axis: str = "intensity",
        color_axis: str = "intensity",
        cmap: str = "viridis",
        alpha: float = 0.1,
    ):
        if self.get_plotting_engine() == "bokeh":
            raise NotImplementedError(
                "3D plots are not supported in bokeh. Please use plotly or matplotlib."
            )
        else:
            return hv.Scatter3D(
                data=dataframe,
                kdims=[x_axis, y_axis, z_axis],
                vdims=[color_axis],
            ).opts(color=color_axis, cmap=cmap, alpha=alpha)
