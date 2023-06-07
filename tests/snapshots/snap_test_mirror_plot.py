# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestMirrorPlot.test_basic[bokeh] 1'] = GenericRepr(':Overlay\n   .Curve.Top_test    :Curve   [m/z]   (intensity)\n   .Curve.Bottom_test :Curve   [m/z]   (intensity)\n   .HLine.I           :HLine   [x,y]')

snapshots['TestMirrorPlot.test_basic[matplotlib] 1'] = GenericRepr(':Overlay\n   .Curve.Top_test    :Curve   [m/z]   (intensity)\n   .Curve.Bottom_test :Curve   [m/z]   (intensity)\n   .HLine.I           :HLine   [x,y]')

snapshots['TestMirrorPlot.test_basic[plotly] 1'] = GenericRepr(':Overlay\n   .Curve.Top_test    :Curve   [m/z]   (intensity)\n   .Curve.Bottom_test :Curve   [m/z]   (intensity)\n   .HLine.I           :HLine   [x,y]')
