#!/usr/bin/env python

import sys, os, subprocess
from processing_obj import Qprocess
import layers
import qgis.core as qgc
import os

qgpy = Qprocess()

p = qgpy.getp() 


def clip_raster(in_raster, polygon_mask, out_raster):
	subprocess.call(['gdalwarp', '-q', '-cutline', polygon_mask, '-dstalpha',  '-of', 'GTiff', 
					 in_raster, out_raster])
	
	
