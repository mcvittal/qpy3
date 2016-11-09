#!/usr/bin/env python2

import sys, os, platform


# Creates a dummy QGIS interface for the processing objects to interact with
class DummyInterface(object):
	def __init__(self):
		self.destCrs = None
	def __getattr__(self, *args, **kwargs):
		def dummy(*args, **kwargs):
			return DummyInterface()
		return dummy
	def __iter__(self):
		return self
	def next(self):
		raise StopIteration
	def layers(self):
		# simulate iface.legendInterface().layers()
		return qgis.core.QgsMapLayerRegistry.instance().mapLayers().values()
	

def get_qgisprefix():
	this_os = platform.platform().lower()
	if "windows" in this_os:
		print "Initializing for a Windows system"
		qgis_folder = None
		is_osgeo = True
		
		if os.path.isdir(r"C:\OSGeo4W\apps\qgis\python\plugins"):
			return r"C:\OSGeo4W\apps\qgis"
		elif os.path.isdir(r"C:\OSGeo4W\apps\qgis-ltr\python\plugins"):
			return r"C:\OSGeo4W\apps\qgis-ltr"
		elif os.path.isdir(r"C:\OSGeo4W64\apps\qgis\python\plugins"):
			return r"C:\OSGeo4W64\apps\qgis"
		elif os.path.isdir(r"C:\OSGeo4W64\apps\qgis-ltr\python\plugins"):
			return r"C:\OSGeo4W64\apps\qgis-ltr"
		elif os.path.isdir(r"C:\Program Files (x86)"):
			is_osgeo = False
			qgis_folder = ""
			for folder in os.listdir(r"C:\Program Files (x86)"):
				if "QGIS" in folder.upper():
					return os.path.join(r"C:\Program Files (x86)", folder)
			if qgis_folder == "" or qgis_folder == None:
				for folder in os.listdir(r"C:\Program Files"):
					if "QGIS" in folder.upper():
						return os.path.join(r"C:\Program Files", folder)
			if qgis_folder == "":
				print("Could not find QGIS installation.")
				print("Please email alexander.mcvittie@gmail.com for assistance")
				sys.exit(0)
		else:
			is_osgeo = False
			qgis_folder = ""
			for folder in os.listdir(r"C:\Program Files"):
				if "QGIS" in folder.upper():
					return os.path.join(r"C:\Program Files", folder)
				
			# Location of QGIS installation has been found. 
			# If it hasnt been found yet, it means it's not installed or they have
			# a custom setup. If the latter is the case, I'll need to add an
			# exception to the code.
			if qgis_folder == "":
				print("Could not find QGIS installation.")
				print("Please email alexander.mcvittie@gmail.com for assistance")
				sys.exit(0)
			qgis_base = qgis_folder

			if not is_osgeo and "qgis-ltr" in os.listdir(os.path.join(qgis_base, "apps")):
				return os.path.join(qgis_base, "apps", "qgis-ltr")
			elif not is_osgeo:
				return os.path.join(qgis_base, "apps", "qgis")
	else:
		return "/usr"
def init_path():
	this_os = platform.platform().lower()
	prefix = get_qgisprefix()
	if "windows" in this_os:
		qgis_subdir = "qgis"
		if os.path.isdir(os.path.join(prefix, r"apps\qgis-ltr")):
			qgis_subdir = "qgis-ltr"
			
		sys.path.append(os.path.join(prefix, "apps", qgis_subdir, "python"))
		sys.path.append(os.path.join(prefix, "apps", qgis_subdir, r"python\plugins"))
		sys.path.append(os.path.join(prefix, "apps"))
		sys.path.append(os.path.join(prefix, "bin"))
		return os.path.join(prefix, "apps", qgis_subdir)
		
	else:
		os.environ['PATH'] = qgisprefix + '/bin'
		os.environ['LD_LIBRARY_PATH'] = qgisprefix+'/lib'
		#Allows for stderr and stdout to be printed to screen - QGIS swallows it otherwise 
		sys.path.insert(0, qgisprefix+'/share/qgis/python')
		sys.path.insert(1, qgisprefix+'/share/qgis/python/plugins')
		return "/usr"

		
# Configure the stuff that differs between operating systems.
qgsapplication_prefix = init_path()

# Standard configuration
os.environ['QGIS_DEBUG'] = '-1'

# Imports
from qgis.core import *
from qgis.gui import *


def init_qprocess():
	QgsApplication.setPrefixPath(qgsapplication_prefix, True)
	app = QgsApplication([], True)
	QgsApplication.initQgis()
	from PyQt4 import QtCore, QtGui
	import processing
	from processing.core.Processing import Processing
	from processing.tools import general as g

	# Create a dummy QGIS interface. Requires an X server connection in linux to run.
	iface = DummyInterface()
	plugin = processing.classFactory(iface)
	Processing.initialize()
	return g

class Qprocess():
	def __init__(self):
		pass
	def getp(self):
		return init_qprocess()