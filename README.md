# qpy3

Standalone open source python module for spatial analysis and GIS processing.

## What is it? 

I've found that standalone GIS processing to be quite a chore in the open source world, coming from being a heavy ESRI user in university, and wanting to transition away from closed source GIS processing to a fully open stack. This is intended to be a drop-in replacement for ESRI's closed source, Windows only `arcpy` python library. The goal of this project is to reach as close to feature parity as possible, enabling a user to replace `import arcpy` with `from qpy3 import Qpy as arcpy` at the top of their script, and have identical outputs to their ArcPy script. This module works with Python 3 and QGIS 3.10. QGIS 3.4 works, but spews a lot of deprecation warnings. 

# Setup

On Ubuntu, simply run setup.sh. It will install the necessary dependencies. xvfb and xvfbwrapper create a dummy graphical interface for running on a headless environment.

An update to this library to work with Windows is coming soon! Stay tuned. 

# Testing

To ensure that it works, run the `test.py` script available in the tests subfolder. It will run some basic geoprocessing tools on the sample data provided in the repo. 


# Contributing

Want to contribute? Simply create a pull request to add new functionality. 

