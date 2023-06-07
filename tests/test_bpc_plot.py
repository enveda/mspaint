from mspaint.plotter import Plotter


class TestXICPlot:
    def test_basic(self, snapshot, engine, plot_data):
        plotter = Plotter(plotting_engine=engine)
        plot = plotter.make_bpc_plot(
            bpc_dataframe=plot_data,
            intensity_column="intensity",
            rt_column="rt",
        )
        snapshot.assert_match(plot)
