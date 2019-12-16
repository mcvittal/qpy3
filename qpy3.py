#!/usr/bin/env python3

## Main class that handles imports of all sub-classes. 

## Written 12/12/2019 by @mcvittal
from modules.SetPaths import SetPaths
setPaths = SetPaths()


from modules.Analysis import Analysis
from modules.License import LicenseManager
from modules.RasterProcessing import RasterProcessingToolset


import sys
from qgis.core import QgsApplication, QgsVectorLayer


gui_flag = False

# For headless servers - fake x server so dummy QGIS instance can run
if not setPaths.isWindows():
    from xvfbwrapper import Xvfb
    vdisplay = Xvfb()
    vdisplay.start()

#Create dummy instance 
app = QgsApplication([], gui_flag)

# Instantiate the dummy instance
QgsApplication.setPrefixPath(setPaths.get_qgisprefix(), True)
QgsApplication.initQgis()



# Load processing package
from processing.core.Processing import Processing
import processing
Processing.initialize()

class Qpy(Analysis, LicenseManager, RasterProcessingToolset):
    def close(self):
        # Exit applications
        QgsApplication.exitQgis()
        QgsApplication.exit()

    # Helpful general functions go here
    def list_all_algorithms(self, search_str=""):
        search_str = search_str.lower()
        for alg in QgsApplication.processingRegistry().algorithms():
            if search_str in alg.name().lower() or search_str in alg.displayName().lower():
                print("{}:{} --> {}".format(alg.provider().name(), alg.name(), alg.displayName()))

    def algorithmHelp(self, name):
        processing.algorithmHelp(name)


Qpy = Qpy(processing, Processing)