#!/usr/bin/env python

import sys
from processing_obj import Qprocess
from qgis.core import QgsRasterLayer
import qgis.core as qgc

qgpy = Qprocess()

p = qgpy.getp()

# create_shp: String -> QgsVectorLayer
# Easily create a QGIS vector shapefile layer.
# Sets name to be the filename without extension.

def create_shp(shpfile_path):
	lyr = qgc.QgsVectorLayer(shpfile_path, shpfile_path[:-4], "none")
	if not lyr.isValid():
		print "Invalid layer. Bailing out, good luck."
		return lyr
		#sys.exit(0)
	else:
		return lyr


# create_raster: String -> QgsRasterLayer
# Easily create a QGIS raster layer.
def create_raster(raster_path):
	fileinfo = QFileInfo(raster_path)
	baseName = fileInfo.baseName()
	path = fileInfo.filePath()
	if (baseName and path):
		raster = QgsRasterLayer(path, baseName)
	return raster

