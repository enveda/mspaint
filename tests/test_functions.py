import numpy as np

from mspaint.functions import make_gapped_array

INPUT_ARRAY = [2, 3]


def test_make_gapped_array():
    assert np.array_equal(make_gapped_array(INPUT_ARRAY), [0, 2, 2, 0, 3, 3])


def test_make_gapped_array_negative():
    assert np.array_equal(
        make_gapped_array(INPUT_ARRAY, negative=True), [0, -2, -2, 0, -3, -3]
    )


def test_make_gapped_array_ones_no_negative():
    assert np.array_equal(
        make_gapped_array(INPUT_ARRAY, intensities=True, negative=False),
        [np.nan, 0, 2, np.nan, 0, 3],
        equal_nan=True,
    )
