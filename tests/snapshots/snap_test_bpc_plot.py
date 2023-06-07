# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestXICPlot.test_basic[bokeh] 1'] = GenericRepr(':Curve   [rt]   (intensity)')

snapshots['TestXICPlot.test_basic[matplotlib] 1'] = GenericRepr(':Curve   [rt]   (intensity)')

snapshots['TestXICPlot.test_basic[plotly] 1'] = GenericRepr(':Curve   [rt]   (intensity)')
