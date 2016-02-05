from processing_obj import Qprocess
import qgis.core as qgc

qgpy = Qprocess()

p = qgpy.getp()

# create_shp: String -> None
# Easily create a QGIS vector shapefile layer.
# Sets name to be the filename without extension.

def create_shp(shpfile_path):
	return qgc.QgsVectorLayer(shpfile_path, shpfile_path[:-4], "http://www.google.ca")

def create_raster(raster_path):
	return qgc.QgsRasterLayer(raster_path, raster_path[:-4], "http://www.google.ca")

