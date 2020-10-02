#!/usr/bin/env python3

## Main class that handles imports of all sub-classes. 

## Written 12/12/2019 by @mcvittal
from modules.Utils.SetPaths import SetPaths
setPaths = SetPaths()


from modules.Vector.Analysis import Analysis
from modules.Utils.License import LicenseManager
from modules.Raster.RasterProcessing import RasterProcessingToolset
from modules.Vector.Overlay import Overlay

from qgis.core import QgsApplication

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

class Qpy(Analysis, LicenseManager, Overlay, RasterProcessingToolset):
    def close(self):
        # Exit applications
        QgsApplication.exitQgis()
        QgsApplication.exit()

    # Helpful general functions go here
    def alglist(self, search_str=""):
        search_str = search_str.lower()
        for alg in QgsApplication.processingRegistry().algorithms():
            if search_str in alg.name().lower() or search_str in alg.displayName().lower():
                print("{}:{} --> {}".format(alg.provider().name(), alg.name(), alg.displayName()))

    def alghelp(self, name):
        processing.algorithmHelp(name.lower())


Qpy = Qpy(processing, Processing)