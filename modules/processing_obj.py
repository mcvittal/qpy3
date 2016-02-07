#!/usr/bin/python
#   Prepare the environment
import sys, os
# Setup path to processing modules
qgisprefix = '/usr'

os.environ['PATH'] = qgisprefix + '/bin'
os.environ['LD_LIBRARY_PATH'] = qgisprefix+'/lib'
sys.path.insert(0, qgisprefix+'/share/qgis/python')
sys.path.insert(1, qgisprefix+'/share/qgis/python/plugins')
#Allows for stderr and stdout to be printed to screen.

#uninstallErrorHook()
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
		
