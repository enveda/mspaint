import pytest


class TestXICPlot:
    def test_with_mz_range(self, snapshot, plotter, plot_data):
        plot = plotter.make_xic_plot(
            xic_dataframe=plot_data,
            mz_range=(311, 312),
            intensity_column="intensity",
            mz_column="mz",
            rt_column="rt",
        )
        snapshot.assert_match(plot)

    def test_with_mz_value_and_tolerance(self, snapshot, plotter, plot_data):
        plot = plotter.make_xic_plot(
            xic_dataframe=plot_data,
            mz_value=311.5,
            mz_tolerance=0.5,
            intensity_column="intensity",
            mz_column="mz",
            rt_column="rt",
        )
        snapshot.assert_match(plot)

    def test_no_mz_range_or_mz_value(self, plotter, plot_data):
        """Should raise a ValueError."""
        with pytest.raises(ValueError):
            plotter.make_xic_plot(
                xic_dataframe=plot_data,
                intensity_column="intensity",
                mz_column="mz",
                rt_column="rt",
            )

    def test_missing_mz_tolerance(self, plotter, plot_data):
        """Should raise a ValueError."""
        with pytest.raises(ValueError):
            plotter.make_xic_plot(
                xic_dataframe=plot_data,
                mz_value=311.5,
                intensity_column="intensity",
                mz_column="mz",
                rt_column="rt",
            )
