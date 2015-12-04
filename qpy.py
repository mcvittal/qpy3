<<<<<<< HEAD
=======
###
###
### You are free to modify this script to fit your needs.
### 
###

>>>>>>> 8ec145762323524c1c55e5ab7924c47fd156a113

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

QgsApplication.setPrefixPath("/usr", True)
QgsApplication.initQgis()
import processing as p

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
iface = DummyInterface()
plugin = p.classFactory(iface) 

def runalg(*arg):
	arguments = arg
	p.runalg(*arguments)

def alglist(*arg):
	arguments = arg
	p.alglist(*arguments)

def alghelp(algorithm):
	p.alghelp(algorithm)

def algoptions(algorithm):
	p.algoptions(algorithm)

def getobj(obj):
	return p.getobject(obj)

def values(*arg):
	return p.values(*arg)

def getfeatures(layer):
	return p.getfeatures(layer)

def uniquelabels(*arg):
	return p.uniquelabels(*arg)



def close():
	# Exit applications
	QgsApplication.exitQgis()
	QApplication.exit()
