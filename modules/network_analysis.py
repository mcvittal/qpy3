#!/usr/bin/env python2

import qgis.core as qgc
import layers
import sys, os


# Code modified from http://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/network_analysis.html#areas-of-availability
def serviceAreas(line_network, starting_point):
	v1 = layers.create_shp(line_network)
	director = QgsLineVectorLayerDirector(vl, -1, '', '', '', 3)
	properter = QgsDistanceArcProperter()
	director.addProperter(properter)
	delta = qgis.utils.iface.mapCanvas().getCoordinateTransform().mapUnitsPerPixel() * 1
	
	# Get the CRS of the line network 
	crs = v1.crs().authid()
	builder = QgsGraphBuilder(crs)
	pStart = layers.create_shp(starting_point)
	
	