# qpy3

Standalone open source python module for spatial analysis and GIS processing.

## What is it? 

I've found that standalone GIS processing to be quite a chore in the open source world, coming from being a heavy ESRI user in university, and wanting to transition away from closed source GIS processing to a fully open stack. This is intended to be a drop-in replacement for ESRI's closed source, Windows only `arcpy` python library. The goal of this project is to reach as close to feature parity as possible, enabling a user to replace `import arcpy` with `from qpy3 import Qpy as arcpy` at the top of their script, and have identical outputs to their ArcPy script. This module works with Python 3 and QGIS 3.10. QGIS 3.4 works, but spews a lot of deprecation warnings. 

# Setup

## Ubuntu

On Ubuntu, simply run setup.sh. It will install the necessary dependencies. xvfb and xvfbwrapper create a dummy graphical interface for running on a headless environment. 

## Windows 

Currently, this library does not support "true" standalone processing in Windows, but rather must be used within the OSGeo4W Python shell. You can invoke your qpy script by calling `python-qgis my_qpy_script.py`  from within the OSGeo4W shell. We simply do not have the resources to make true standalone qpy happen on Windows, but we will gladly accept a pull request that enables this! 

## MacOS

Nobody on the development team currently owns a mac or hackintosh, so we are unable to develop for this operating system. We assume that it would only be a minor change to how it works on Linux. A pull request enabling this feature would be readily accepted. 

# Using the library 

Example: Buffer your data

```
from qpy3 import Qpy 

distance = 2 # decimal degrees in a geographic CRS, meters in a projected CRS

in_shp = "/path/to/shapefile.shp"

out_shp = "/path/to/output/shapefile.shp"

Qpy.Buffer(in_shp, out_shp, distance)

# Close the dummy QGIS instance
Qpy.close()
```

# Testing

To ensure that it works, run the `test.py` script available in the tests subfolder. It will run some basic geoprocessing tools on the sample data provided in the repo. 


# Contributing

Want to contribute? Simply create a pull request to add new functionality. 

