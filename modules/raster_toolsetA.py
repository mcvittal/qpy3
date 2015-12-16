import sys, os
from processing_obj import Qprocess
import layers
import qgis.core as qgc
import os

qgpy = Qprocess()

p = qgpy.getp() 


def clip_raster(in_raster, polygon_mask, out_raster):
	in_raster = layers.create_raster(in_raster)
	polygon_mask = layers.create_shp(polygon_mask)
	p.runalg("saga:clipgridwithpolygon", in_raster,polygon_mask,out_raster)

