#!/usr/bin/env python3

## Main class that handles imports of all sub-classes. 

## Written 12/12/2019 by @mcvittal
from modules.SetPaths import SetPaths
setPaths = SetPaths()


from modules.Analysis import Analysis
from modules.License import LicenseManager


import sys
from qgis.core import QgsVectorLayer, QgsApplication

gui_flag = False

# For headless servers - fake x server so dummy QGIS instance can run
if not setPaths.isWindows():
    from xvfbwrapper import Xvfb
    vdisplay = Xvfb()
    vdisplay.start()

#Create dummy instance 
print("it imported")
app = QgsApplication([], gui_flag) # THIS IS WHERE IT IS BROKEN
print('didn\'t died on the application')

# Instantiate the dummy instance
QgsApplication.setPrefixPath(setPaths.get_qgisprefix(), True)
QgsApplication.initQgis()



# Load processing package
from processing.core.Processing import Processing
import processing
Processing.initialize()

class Qpy(Analysis, LicenseManager):
    def close(self):
        # Exit applications
        QgsApplication.exitQgis()
        QgsApplication.exit()

Qpy = Qpy(processing, Processing)


# Helpful general functions go here 
def list_all_algorithms(self):
    for alg in QgsApplication.processingRegistry().algorithms():
        print("{}:{} --> {}".format(alg.provider().name(), alg.name(), alg.displayName()))



