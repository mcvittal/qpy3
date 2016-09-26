#!/usr/bin/env python
#   Prepare the environment
import sys, os, platform

# Determine what OS is being used
this_os = platform.platform().lower()
if "windows" in this_os:
	print "Initializing qpy for a Windows system"
	qgisprefix = 'C:/OSGeo4W64/bin'
	os.system("windows_init.bat")
	os.system("'C:\Program Files\QGIS 2.14\apps\Python27\Lib\site-packages\pythonwin\pywin\framework\startup.py'")
	os.environ['PATH'] = "'C:\Program Files\QGIS 2.14\apps\qgis-ltr\bin'"


else:
	print "Initializing qpy for a Linux system"
	# Setup path to processing modules
	qgisprefix = '/usr'
	# Set up the environment path settings, append QGIS library locations 
	os.environ['PATH'] = qgisprefix + '/bin'
	os.environ['LD_LIBRARY_PATH'] = qgisprefix+'/lib'
	#Allows for stderr and stdout to be printed to screen - QGIS swallows it otherwise 
	sys.path.insert(0, qgisprefix+'/share/qgis/python')
	sys.path.insert(1, qgisprefix+'/share/qgis/python/plugins')

#uninstallErrorHook() # Needed it for earlier versions of QGIS 
os.environ['QGIS_DEBUG'] = '-1'

#Package imports
from qgis.core import *
from qgis.gui import *

QgsApplication.setPrefixPath(qgisprefix, True)
app = QgsApplication([], True)
from PyQt4 import QtCore, QtGui
import processing 
from processing.core.Processing import Processing
from processing.tools import general as g


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

# The class that gets created in all subsequent qpy modules.
#     Creates a processing object and allows other .py classes
#     and methods to obtain it.
class Qprocess():
	QgsApplication.setPrefixPath("/usr", True)
	iface = DummyInterface()
	plugin = processing.classFactory(iface)
	Processing.initialize()
	def getp(self):
		return g 
	def getqgs(self):
		return QgsApplication
		
