#!/usr/bin/env python
import sys, os, shutil, glob
from processing_obj import Qprocess
import layers
import qgis.core as qgc
import os

# VectorA contains basic functions contained within the base QGIS installation.
#   All calls to the processing object use the qgis: spatial algorithms.
#   Other vector classes in the future will contain calls to addons such as
#   the MMQGIS plugin, GRASS7 libraries, SAGA functions, etc. 
class VectorA():
	def __init__(self, _p=None):
		self.p = _p

	# Clip: String String String --> None
	# 
	# Outputs features from in_shp that intersect clip_shp. 
	#
	# in_shp and clip_shp must both be valid fullpaths to shape files
	# out_shp must be a valid path to a shp file (doesnt have to exist)
	def clip(self, in_shp, clip_shp, out_shp):
		in_shp = layers.create_shp(in_shp)
		clip_shp = layers.create_shp(clip_shp)
		self.p.runalg("qgis:clip", in_shp, clip_shp, out_shp)

	

	# intersect: String String String --> None
	#
	# Generates the intersection between two polygons.
	#
	# in_shp and in_shp2 must be a valid path to a valid ESRI shapefile datatype, and out_shp must be a non-existing ESRI shp file in an actual existing folder
	def intersect(self, in_shp, in_shp2, out_shp):
		in_shp = layers.create_shp(in_shp)
		in_shp2 = layers.create_shp(in_shp2)
		self.p.runalg("qgis:intersection", in_shp, in_shp2, out_shp)
	# erase: String String String --> None
	# 
	# Erases features from the in_shp polygon that overlap the erase_shp polygon.
	#
	# in_shp and erase_shp must be valid paths to ESRI shapefile datatypes, and out_shp must be a non-existing ESRI shp file in an existing folder.
	
	def erase(self, in_shp, erase_shp, out_shp, ignore_invalid=False):
		in_shp = layers.create_shp(in_shp)
		erase_shp = layers.create_shp(erase_shp)
		self.p.runalg("qgis:difference", in_shp, erase_shp, ignore_invalid, out_shp)
	
	# union: in_shp, in_shp2, out_shp --> None
	#
	# Calculates the geometric union between two shapefiles.
	# 
	# in_shp and in_shp2 must be valid paths to ESRI shapefile datatypes, and out_shp must be a non-existing ESRI shp file in an existing folder.
	
	def union(self, in_shp, in_shp2, out_shp):
		in_shp = layers.create_shp(in_shp)
		in_shp2 = layers.create_shp(in_shp2)
		print "ayy"
		self.p.runalg("qgis:union", in_shp, in_shp2, out_shp)
	
	# merge: in_shp, in_shp2, out_shp --> None
	# 
	# Merges two shapefiles into one shapefile. Must be all the same vector type (all polygon, all line, or all point. Cannot take in one point and one line)
	#
	# in_shp and in_shp2 must be valid paths to ESRI shapefile datatypes, and out_shp must be a non-existing ESRI shp file in an existing folder.
	
	def merge(self, in_shp, in_shp2, out_shp):
		self.p.runalg("qgis:mergevectorlayers", in_shp + ";" + in_shp2, out_shp)
	
	# merge_multiple: (list String) String --> None
	#
	# Takes an input list of shapefiles and merges them together. 
	#
	# All strings in the shp_lst argument must be valid paths to existing shapefiles, and they must all be the same vector type (all polygon, all line, or all point. Cannot take in one point and one line). Out_shp must be a non-existing ESRI shp file in an existing folder.
	
	def merge_multiple(self, shp_lst, out_shp):
		shps = ""
		for shp in shp_lst:
			shps += shp + ";"
		shps = shps[:-1]
		self.p.runalg("qgis:mergevectorlayers", shps, out_shp)
	
	# merge_folder: String String Boolean --> None
	#
	# Takes an input directory containing shapefiles and merges all the shapefiles into one shapefile.
	#
	# The directory must be a valid directory containing only one vector type (all polygon, all line, or all point. Cannot take in one point and one line). Out_shp must be a non-existing ESRI shp file in an existing folder.
	
	def merge_folder(self, indir, out_shp, recursive=False):
		if not recursive:
			lst = glob.glob(os.path.join(indir, "*.shp"))
		else:
			pass
		merge_multiple(lst, out_shp)
		
	# add_field: String String (union "integer" "float" "string") Integer Float String --> None
	#
	# Takes an input shapefile and adds a field - either Integer, Float or String type.
	#
	# Must be a valid shapefile. field_name must be a non-existent field in in_shp. Out_shp must be a non-existing ESRI shp file in an existing folder.

	def add_field(self, in_shp, field_name, field_type, field_length, field_precision, output_layer):
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
		self.p.runalg("qgis:addfieldtoattributestable", in_shp, field_name, field_type, field_length, field_precision, output_later)

	# count_points_in_polygon: String String String String --> None
	# 
	# Takes an input point cloud and an input polygon layer, and produces an output polygon layer with a new field containing how many points from the point cloud fall within each polygon.
	# 
	# Must be a valid point shapefile and a valid polygon shapefile. count_field must a non-existent field in the in_polygon attribute table. Out_shp must be a non-existing ESRI shp file in an existing folder.
	
	def count_points_in_polygon(self, in_polygon, in_points, count_field, out_polygon):
		in_polygon = layers.create_shp(in_polygon)
		in_points = layers.create_shp(in_points)
		self.p.runalg("qgis:countpointsinpolygon", in_polygon, in_points, count_field, out_polygon)
		
	# count_unique_points_in_polygon: String String String String String --> None
	#
	# Takes an input point cloud and an input polygon layer, and produces an output polygon layer with a new field containing how many points from the point cloud fall within each polygon. Also uses a unique field argument so that items of the same property are not double-counted.
	#
	# Must be a valid point shapefile and a valid polygon shapefile. unique_field must be aan existing field in the in_points attribute table. count_field must a non-existent field in the in_polygon attribute table. Out_shp must be a non-existing ESRI shp file in an existing folder.
	def count_unique_points_in_polygon(self, in_polygon, in_points, unique_field, count_field, out_polygon):
		in_polygon = layers.create_shp(in_polygon)
		in_points = layers.create_shp(in_points)
		self.p.runalg("qgis:countuniquepointsinpolygon", in_polygon, in_points, unique_field, count_field, out_polygon)
	# distance_matrix: String String String String Integer Integer String --> None
	#
	# Produces a near table in CSV format between two point cloud datasets. 
	
	def distance_matrix(self, in_points, in_field, target_points, target_field, matrix_type, nearest_points, output_table):
		in_points = layers.create_shp(in_points)
		target_points = layers.create_shp(target_points)
		self.p.runalg("qgis:distancematrix", in_points, in_field, target_points, target_field, matrix_type, nearest_points, output_table)
	# generate_points_along_line_pixel: String String String --> None
	#
	# Produces points along a line, but they are the centroids of the pixels the line passes through, not necessarily directly on the line.
	#
	# 
	def generate_points_along_line_pixel(self, in_line, in_raster, out_points):
		in_line = layers.create_shp(in_line)
		in_raster = layers.create_raster(in_raster)
		self.p.runalg("qgis:generatepointspixelcentroidsalongline", in_line, in_raster, out_points)
	def generate_points_inside_polygon_pixel(self, in_polygon, in_raster, out_points):
		in_polygon = layers.create_shp(in_polygon)
		in_raster = layers.create_raster(in_raster)
		self.p.runalg("qgis:generatepointspixelcentroidsinsidepolygons", in_polygon, in_raster, out_points)
	def hublines(self, in_hub_points, hub_id_field, in_spoke_points, spoke_id_field, out_hub_lines):
		in_hub_points = layers.create_shp(in_hub_points)
		in_spoke_points = layers.create_shp(in_spoke_points)
		self.p.runalg("qgis:hublines", in_hub_points, hub_id_field, in_spoke_points, spoke_id_field, out_hub_lines)
	def mean_coordinates(self, in_points, out_point, in_weightfield=None, in_uniquefield=None,):
		in_points = layers.create_shp(in_points)
		self.p.runalg("qgis:meancoordinates", in_points, in_weightfield, in_uniquefield, out_point)
	def nearest_neighbour(self, in_points, out_html):
		in_points = layers.create_shp(in_points)
		self.p.runalg("qgis:nearestneighbouranalysis", in_points, out_html)
	def sum_line_lengths(self, in_lines, in_polygons, out_lines, length_field="LENGTH", count_field="COUNT"):
		in_lines = layers.create_shp(in_lines)
		in_polygons = layers.create_shp(in_polygons)
		p.runalg("qgis:sumlinelengths", in_lines, in_polygons, length_field, count_field, out_lines)
	
	def create_vectorgrid(self, extent_layer, grid_x, grid_y, type, out_vector):
                pass

# VectorB contains functions that require the use of OGR functions (Select)

class VectorB():
	def __init__(self, _p=None):
		self.p = _p
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
