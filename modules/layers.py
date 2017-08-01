#!/usr/bin/env python

import sys
from processing_obj import Qprocess
from PyQt4.QtCore import QFileInfo,QSettings
from qgis.core import QgsRasterLayer
from qgis.networkanalysis import *
import qgis.core as qgc
from qgis.gui import QgisInterface

# create_shp: String -> QgsVectorLayer
# Easily create a QGIS vector shapefile layer.
# Sets name to be the filename without extension.
class Layers():
	def __init__(self, _p=None):
		self.p = _p
		
	# create_crs: Int -> QgsCoordinateReferenceSystem
	# Takes in a CRS ID and returns the appropriate CRS Object.
	def create_crs(self, crsID):
		crs = qgc.QgsCoordinateReferenceSystem()
		crs.createFromId(crsID)
		return crs
	
	def create_shp(self, shpfile_path, crsID=None):
		fileInfo = QFileInfo(shpfile_path)
		baseName = fileInfo.baseName()
		
		try:
			layer = qgc.QgsVectorLayer(shpfile_path, baseName, "none")
		except:
			layer = qgc.QgsVectorLayer(shpfile_path, baseName, "none")
		sourceCrs = layer.crs()
		destCrs = None
		if crsID == None:
			destCrs = qgc.QgsCoordinateReferenceSystem(4326)
		else:
			destCrs = qgc.QgsCoordinateReferenceSystem(crsID)
		
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
			layer.setCrs(crs)
			return layer 
		else:
			return layer
	# create_table: String -> None 
	
	
	def create_table(self, table_path):
		fileInfo = QFileInfo(table_path)
		baseName = fileInfo.baseName()
		path = fileInfo.filePath()
	
	def get_bounding(self, layer):
		#QgsMapLayerRegistry.instance().addMapLayer(layer)
		extent = layer.extent()
		xmin = extent.xMinimum()
		xmax = extent.xMaximum()
		ymin = extent.yMinimum()
		ymax = extent.yMaximum()
		return "{},{},{},{}".format(xmin, xmax, ymin, ymax)
	
	def get_qgc(self):
		return qgc
	
	def get_interface(self):
		iface = QgisInterface
		return iface
	
	
	
	
	# create_graph: String -> QgsLineVectorLayerDirector
	# Creates a graph out of a line network shapefile for use with the class network_analysis.py.
	# Currently treats all roads as 2 way roads. 
	
	def create_graph(self, line_network_path):
		line_lyr = create_shp(line_network_path)
		director = QgsLineVectorLayerDirector(line_lyr, -1, '', '', '', 3)
		return director
