#!/usr/bin/env python3

import sys, traceback

sys.path.append("..")

from qpy3 import Qpy

print("Testing buffering")

try:
    Qpy.Buffer("../test_data/point1.shp", "test_output/buffered.shp", 0.5)
    print("Buffering succeeded")
except Exception:
    traceback.print_exc(file=sys.stdout)
    
    
print("Testing completed. Closing QGIS object")
Qpy.close()
