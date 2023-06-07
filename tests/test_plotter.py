import pytest

from mspaint.plotter import Plotter


class TestPlotter:
    """Test Plotter."""

    def test_bad_engine(self):
        """Should raise a ValueError and mention all engine choices."""
        with pytest.raises(ValueError) as exc_info:
            Plotter(plotting_engine="very_nonsensical")

        _error_message = str(exc_info.value)
        for engine in Plotter.ENGINES:
            assert engine in _error_message
