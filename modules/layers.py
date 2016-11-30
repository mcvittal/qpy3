#!/usr/bin/env python

import sys
from processing_obj import Qprocess
from qgis.core import QgsRasterLayer
from qgis.networkanalysis import *
import qgis.core as qgc

# create_shp: String -> QgsVectorLayer
# Easily create a QGIS vector shapefile layer.
# Sets name to be the filename without extension.

def create_shp(shpfile_path):
	return qgc.QgsVectorLayer(shpfile_path, shpfile_path[:-4], "none")
	
# create_raster: String -> QgsRasterLayer
# Easily create a QGIS raster layer.
def create_raster(raster_path):
	fileinfo = QFileInfo(raster_path)
	baseName = fileInfo.baseName()
	path = fileInfo.filePath()
	if (baseName and path):
		raster = QgsRasterLayer(path, baseName)
	return raster

	
# create_graph: String -> QgsLineVectorLayerDirector
# Creates a graph out of a line network shapefile for use with the class network_analysis.py.
# Currently treats all roads as 2 way roads. 
def create_graph(line_network_path):
	line_lyr = create_shp(line_network_path)
	director = QgsLineVectorLayerDirector(line_lyr, -1, '', '', '', 3)
	return director
