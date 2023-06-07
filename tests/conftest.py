import pandas as pd
import pytest

from mspaint.plotter import Plotter


@pytest.fixture(params=["bokeh", "matplotlib", "plotly"])
def engine(request):
    return request.param


@pytest.fixture
def plot_data():
    df = pd.read_parquet("example_data/example_xic_data.pt")
    return df


@pytest.fixture
def plotter(engine):
    return Plotter(plotting_engine=engine)
