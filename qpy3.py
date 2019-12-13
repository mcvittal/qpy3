#!/usr/bin/env python3

## The new home for qpy - qpy2. The old qpy is slated for removal and will be replaced with this
## class.

## Written 12/12/2019 by @mcvittal

from modules2.Analysis import Analysis

import sys
from qgis.core import QgsApplication, QgsVectorLayer
gui_flag = False
app = QgsApplication([], gui_flag)
QgsApplication.setPrefixPath("/usr", True)
QgsApplication.initQgis()
sys.path.append('/usr/share/qgis/python/plugins')
# Load processing package
from processing.core.Processing import Processing
import processing
Processing.initialize()

A = Analysis(processing, Processing)



'''
processing.algorithmHelp("gdal:buffervectors")

vlayer = QgsVectorLayer("test_data/point1.shp", "Test layer", "ogr")
params = {}
params["INPUT"] = vlayer
params["DISTANCE"] = 1
params["DISSOLVE"] = True
params["OUTPUT"] = "/tmp/out.shp"
#processing.run("gdal:buffervectors", params)
'''




    #processing.run("qgis:creategrid")
    #for alg in QgsApplication.processingRegistry().algorithms():
    #    print("{}:{} --> {}".format(alg.provider().name(), alg.name(), alg.displayName()))



    #print("unable to load processing")
    #print("unable to load processing")