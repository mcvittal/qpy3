#!/usr/bin/python
# Prepare the environment
import sys
# Specify path to processing module 
sys.path.append('/usr/share/qgis/python/plugins')

# Necessary imports
import qgis
from qgis.utils import *

#Allows for stderr and stdout to be printed to screen.
uninstallErrorHook()

from qgis.core import QgsApplication
import qgis.core as qgc
from qgis.analysis import *
from PyQt4.QtGui import QApplication
app = QApplication([], True)
import processing as p
uninstallErrorHook() 


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
	QgsApplication.initQgis()
	iface = DummyInterface()
	plugin = p.classFactory(iface)
	def getp(self):
		return p 
		
