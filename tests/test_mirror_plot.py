import numpy as np
import pytest

from mspaint.plotter import Plotter


@pytest.fixture
def mirror_plot_data():
    mz1 = np.array([100, 200, 300, 400, 500])
    mz2 = np.array([100, 200, 300, 400, 500])
    int1 = np.array([1, 2, 3, 4, 5])
    int2 = np.array([5, 4, 3, 2, 1])
    return mz1, int1, mz2, int2


class TestMirrorPlot:
    def test_basic(self, snapshot, engine, mirror_plot_data):
        plotter = Plotter(plotting_engine=engine)
        mz1, int1, mz2, int2 = mirror_plot_data

        plot = plotter.make_mirror_plot(
            mzs_on_bottom=mz1,
            intensities_on_bottom=int1,
            mzs_on_top=mz2,
            intensities_on_top=int2,
            title="test1",
            label_bottom="bottom_test",
            label_top="top_test",
        )
        snapshot.assert_match(plot)
