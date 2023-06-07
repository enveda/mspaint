from typing import List, Tuple

import numpy as np


def make_gapped_array(
    arr: List, intensities: bool = False, negative: bool = False
) -> np.array:
    """_summary_
    Input arrays
    mzs = [44,45,49,99]
    int = [10,9,13,12] # intensity

    Output arrays
    mzs = [<>,44,44, <>,45,45, <>,49,49, <>,99,99]
    int = [None,0,10, None,0,9, None,0,13, None,0,12] # intensity

    Args:
        arr (List): _description_
        intensities (bool, optional): _description_. Defaults to False.
        negative (bool, optional): _description_. Defaults to False.

    Returns:
        np.array: _description_
    """
    arr = np.array(arr)

    if negative:  # needed for the inverted plot
        arr *= -1

    # [1,2] -> [1,1,1,2,2,2]
    arr = np.repeat(arr, 3)

    if intensities:
        # [2,2,2,3,3,3] -> [0,2,2,0,3,3]
        arr = [np.nan if i % 3 == 0 else x for i, x in enumerate(arr)]
        # [2,2,2,3,3,3] -> [2,0,2,3,0,3]
        arr = [0 if i % 3 == 1 else x for i, x in enumerate(arr)]
        return arr

    arr = [0 if i % 3 == 0 else x for i, x in enumerate(arr)]
    return arr


def normalize_intensities(intensities: np.array, upper_limit=1e7) -> np.array:
    return intensities * upper_limit / max(intensities)


def calculate_range_for_mirror_plot(
    arr1: np.array, arr2: np.array, padding: float
) -> Tuple[int, int]:
    # calculate the range of the x axis [leftmost point - 10, rightmost point + 10]
    r = (
        int(min([min(arr1), min(arr2)]) - padding),
        int(max([max(arr1), max(arr2)]) + padding),
    )
    return r


def setup_plot_data(
    mzs_on_top, intensities_on_top, mzs_on_bottom, intensities_on_bottom
):
    # normalize intensities
    intensities_on_bottom, intensities_on_top = map(
        normalize_intensities, [intensities_on_bottom, intensities_on_top]
    )

    # calculate the range of the x axis [leftmost point - 10, rightmost point + 10]
    # returns a tuple of np.floats
    xaxis_range = calculate_range_for_mirror_plot(mzs_on_bottom, mzs_on_top, 10)

    # plot on bottom
    mzs_on_bottom = make_gapped_array(mzs_on_bottom)
    intensities_on_bottom = make_gapped_array(intensities_on_bottom, True, True)

    # plot on top
    mzs_on_top = make_gapped_array(mzs_on_top)
    intensities_on_top = make_gapped_array(intensities_on_top, True, False)

    return (
        mzs_on_bottom,
        intensities_on_bottom,
        mzs_on_top,
        intensities_on_top,
        xaxis_range,
    )
