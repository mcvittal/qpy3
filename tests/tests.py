#!/usr/bin/env python3

import sys, traceback, os

sys.path.append("..")

from qpy3 import Qpy


if not os.path.exists("test_output"):
    os.mkdir("test_output")

try:
    print("Testing buffering")
    Qpy.Buffer("test_data/point1.shp", "test_output/buffered.shp", 0.5)
    print("Buffering succeeded")
except Exception:
    traceback.print_exc(file=sys.stdout)
    
try:
    print("Testing selection")
    Qpy.Select_analysis("test_data/multiple_polygons.shp", "test_output/selected.shp", '"id" >=10')
    print("Selection succeeded")
except Exception:
    traceback.print_exc(file=sys.stdout)

try:
    print("testing clip")
    Qpy.Clip_analysis("test_data/multiple_polygons.shp", "test_data/multiple_polygons2.shp", "test_output/clipped.shp")
except Exception:
    traceback.print_exc(file=sys.stdout)

print("Testing completed. Closing QGIS object")
Qpy.close()
