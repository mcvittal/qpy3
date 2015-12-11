import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)))
from processing_obj import Qprocess
import layers
import qgis.core as qgc
import os

qgpy = Qprocess()

p = qgpy.getp() 

# Clip: String String String --> None
# 
# in_shp and clip_shp must both be valid fullpaths to shape files
# out_shp must be a valid path to a shp file (doesnt have to exist)
def Clip(in_shp, clip_shp, out_shp):
	in_shp = layers.create_shp(in_shp)
	clip_shp = layers.create_shp(clip_shp)
	p.runalg("qgis:clip", in_shp, clip_shp, out_shp)

#select: String String String --> None
#
# in_shp must be a valid fullpath to a shape file
# out_shp must be a valid path to a shp file. If it exists, it is overwritten.

def select(in_shp, out_shp, query):
	# Sample query is '"FIELDNAME" = \'value\' '
	# Get in_shp filename
	in_filename = in_shp.split("/")[len(in_shp.split("/")) - 1][:-4]
	out_filename = out_shp.split("/")[len(in_shp.split("/")) - 1][:-4]
	out_path = out_shp[:-(len(out_filename) + 4)]
	# ogr2ogr doesn't like overwriting output, so this removes 
	#    all the related out_shp shapefile files.
	if os.path.exists(out_shp):
		for afile in os.listdir(out_path):
			if afile.startswith(out_filename):
				os.remove(out_path + afile)

	os.system('ogr2ogr -sql "SELECT * FROM ' + in_filename + " WHERE " + query + '" ' + out_shp + " " + in_shp)



def tableselect(in_dbf, out_dbf, query):
	select_analysis(in_dbf, out_dbf, query)



def intersect(in_shp, in_shp2, out_shp):
	in_shp = layers.create_shp(in_shp)
	in_shp2 = layers.create_shp(in_shp2)
	p.runalg("qgis:intersection", in_shp, in_shp2, out_shp)

def erase(in_shp, erase_shp, out_shp):
	in_shp = layers.create_shp(in_shp)
	erase_shp = layers.create_shp(erase_shp)
	p.runalg("qgis:difference", in_shp, erase_shp, out_shp)

def union(in_shp, in_shp2, out_shp):
	in_shp = layers.create_shp(in_shp)
	in_shp2 = layers.create_shp(in_shp2)
	p.runalg("qgis:union", in_shp, in_shp2, out_shp)

	

