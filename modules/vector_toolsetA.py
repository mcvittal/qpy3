#!/usr/bin/env python
import sys, os, shutil, glob
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
def clip(in_shp, clip_shp, out_shp):
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



# tableselect: String String String --> None
#
# in_dbf must be a valid path to a DBF file, and out_dbf must point to a non-existing dbf file in an actual folder.

def tableselect(in_dbf, out_dbf, query):
	select_analysis(in_dbf, out_dbf, query)

# intersect: String String String --> None
#
# in_shp and in_shp2 must be a valid path to a valid ESRI shapefile datatype, and out_shp must be a non-existing ESRI shp file in an actual existing folder
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

def merge(in_shp, in_shp2, out_shp):
	in_shp = layers.create_shp(in_shp)
	in_shp2 = layers.create_shp(in_shp2)
	p.runalg("qgis:mergevectorlayers", in_shp, in_shp2, out_shp)

# merge_multiple: List(String) String -> None
def merge_multiple(shp_lst, out_shp):
	if len(shp_lst) < 3:
		print("Not enough shapefiles in list. Use merge(). Exiting method...")
		return 
	
	# Create a temporary directory that the module will have write access to
	tmpdir = os.path.join(os.path.expanduser("~"), "qgis_tmp") 
	os.mkdir(tmpdir)
	
	# Merge the first two shapefiles in the list
	merge(shp_lst[0], shp_lst[1], os.path.join(tmpdir, "output1.shp"))
	
	# Merge shapefile #3 -> N - 1 together
	for x in range(2, len(shp_lst) - 1):
		merge(shp_lst[x], os.path.join(tmpdir, "output{}.shp".format(x - 1)),
						  os.path.join(tmpdir, "output{}.shp".format(x)))
	
	# Merge the last shapefile in the list
	merge(shp_lst[len(shp_lst) - 1], "output{}.shp".format(len(shp_lst) - 1), out_shp)
	# Delete the temporary directory
	shutil.rmtree(tmpdir)
	
def merge_folder(indir, out_shp):
	lst = glob.glob(os.path.join(indir, "*.shp"))
	merge_multiple(lst, out_shp)
	
	

def add_field(in_shp, field_name, field_type, field_length, field_precision, output_layer):
	in_shp = layers.create_shp(in_shp)
	if field_type.lower() == "integer":
		ft = "integer"
		field_type = 0
	elif field_type.lower() == "float":
		ft = "float"
		field_type = 1
	else:
		ft = "string"
		field_type = 2
	print("Generating field {} of type {}.".format(field_name, ft))	
	p.runalg("qgis:addfieldtoattributestable", in_shp, field_name, field_type, field_length, field_precision, output_later)

