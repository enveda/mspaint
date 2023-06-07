# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestXICPlot.test_with_mz_range[bokeh] 1'] = GenericRepr(':Curve   [rt]   (intensity)')

snapshots['TestXICPlot.test_with_mz_range[matplotlib] 1'] = GenericRepr(':Curve   [rt]   (intensity)')

snapshots['TestXICPlot.test_with_mz_range[plotly] 1'] = GenericRepr(':Curve   [rt]   (intensity)')

snapshots['TestXICPlot.test_with_mz_value_and_tolerance[bokeh] 1'] = GenericRepr(':Curve   [rt]   (intensity)')

snapshots['TestXICPlot.test_with_mz_value_and_tolerance[matplotlib] 1'] = GenericRepr(':Curve   [rt]   (intensity)')

snapshots['TestXICPlot.test_with_mz_value_and_tolerance[plotly] 1'] = GenericRepr(':Curve   [rt]   (intensity)')
