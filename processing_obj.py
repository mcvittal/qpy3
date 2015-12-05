#!/usr/bin/python
# Prepare the environment
import sys
# Prepare processing framework 
sys.path.append('/usr/share/qgis/python/plugins')
import qgis
from qgis.utils import *
uninstallErrorHook()
from qgis.core import QgsApplication
import qgis.core as qgc
from qgis.analysis import *
from PyQt4.QtGui import QApplication
app = QApplication([], True)
import processing as p
uninstallErrorHook() 


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


class Qprocess():
	 
	
	QgsApplication.setPrefixPath("/usr", True)
	QgsApplication.initQgis()
	iface = DummyInterface()
	plugin = p.classFactory(iface)
	def getp(self):
		return p 
		
