#!/usr/bin/env python2

import qgis.core as qgc
import layers
import sys, os


class NetworkAnalysis():
	def __init__(self, p):
		self.p = p
	
	# Code modified from http://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/network_analysis.html#areas-of-availability
	
	def serviceAreas(line_network, starting_point):
		director = layers.create_graph(line_network)
		properter = QgsDistanceArcProperter()
		director.addProperter(properter)
		delta = qgis.utils.iface.mapCanvas().getCoordinateTransform().mapUnitsPerPixel() * 1
		
		# Get the CRS of the line network 
		crs = v1.crs().authid()
		builder = QgsGraphBuilder(crs)
		pStart = layers.create_shp(starting_point)
	
	
class WRPS():
	this.main_results_folder = r"N:\WRPS_open"
	this.main_network = 
	
	
	