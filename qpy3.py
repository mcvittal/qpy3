#!/usr/bin/env python3

## The new home for qpy - qpy3. The old qpy is slated for removal and will be replaced with this
## class.

## Written 12/12/2019 by @mcvittal

from modules.Analysis import Analysis

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

class Qpy(Analysis):
    pass

Qpy = Qpy(processing, Processing)


def list_all_algorithms():
    for alg in QgsApplication.processingRegistry().algorithms():
        print("{}:{} --> {}".format(alg.provider().name(), alg.name(), alg.displayName()))
