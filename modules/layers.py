#!/usr/bin/env python

import sys
from processing_obj import Qprocess
from PyQt4.QtCore import QFileInfo,QSettings
from qgis.core import QgsRasterLayer
from qgis.networkanalysis import *
import qgis.core as qgc

# create_shp: String -> QgsVectorLayer
# Easily create a QGIS vector shapefile layer.
# Sets name to be the filename without extension.
class Layers():
	def __init__(self, _p=None):
		self.p = _p
		
	# create_crs: Int -> QgsCoordinateReferenceSystem
	# Takes in a CRS ID and returns the appropriate CRS Object.
	def create_crs(self, crsID):
		return qgc.QgsCoordinateReferenceSystem(crsID, qgc.QgsCoordinateReferenceSystem.EpsgCrsId)
	
	def create_shp(self, shpfile_path, crs=None):
		fileInfo = QFileInfo(shpfile_path)
		baseName = fileInfo.baseName()
		try:
			layer = qgc.QgsVectorLayer(shpfile_path, baseName, "none")
		except:
			layer = qgc.QgsVectorLayer(shpfile_path, baseName, "none")
		if crs != None:
			crs = qgc.QgsCoordinateReferenceSystem(crs, qgc.QgsCoordinateReferenceSystem.EpsgCrsId)
			layer.setCrs(crs)
			return layer 
		else:
			return layer
		
	# create_raster: String -> QgsRasterLayer
	# Easily create a QGIS raster layer.
	def create_raster(self, raster_path, crs=None):
		fileInfo = QFileInfo(raster_path)
		baseName = fileInfo.baseName()
		path = fileInfo.filePath()
		if (baseName and path):
			layer = QgsRasterLayer(path, baseName)
		if crs != None:
			crs = qgc.QgsCoordinateReferenceSystem(crs, qgc.QgsCoordinateReferenceSystem.EpsgCrsId)
			layer.setCrs(crs)
			return layer 
		else:
			return Layer
	# create_table: String -> 
	
	def create_table(self, table_path):
		fileInfo = QFileInfo(table_path)
		baseName = fileInfo.baseName()
		path = fileInfo.filePath()
	
	def get_bounding(self, layer):
		extent = layer.extent()
		xmin = extent.xMinimum()
		xmax = extent.xMaximum()
		ymin = extent.yMinimum()
		ymax = extent.yMaximum()
		return "{},{},{},{}".format(xmin, xmax, ymin, ymax)
	
	def get_qgc(self):
		return qgc
	
	
	
	
	
	# create_graph: String -> QgsLineVectorLayerDirector
	# Creates a graph out of a line network shapefile for use with the class network_analysis.py.
	# Currently treats all roads as 2 way roads. 
	
	def create_graph(self, line_network_path):
		line_lyr = create_shp(line_network_path)
		director = QgsLineVectorLayerDirector(line_lyr, -1, '', '', '', 3)
		return director
