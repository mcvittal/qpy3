#!/usr/bin/env python
#   Prepare the environment
import sys, os, platform

# Determine what OS is being used
this_os = platform.platform().lower()
qgisprefix = ""

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
					qgis_folder = os.path.join(r"C:\Program Files (x86)",
											   folder)
					break
			if qgis_folder == "":
				for folder in os.listdir(r"C:\Program Files"):
					if "QGIS" in folder.upper():
						qgis_folder = os.path.join(r"C:\Program Files", folder)
						break
			if qgis_folder == "":
				print("Could not find QGIS installation.")
				print("Please email alexander.mcvittie@gmail.com for assistance")
				sys.exit(0)
		else:
			is_osgeo = False
			qgis_folder = ""
			for folder in os.listdir(r"C:\Program Files"):
				if "QGIS" in folder.upper():
					qgis_folder = os.path.join(r"C:\Program Files", folder)
					break
				
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




if "windows" in this_os:
	print "Initializing for a Windows system"
	qgis_folder = None
	is_osgeo = True
	
	if os.path.isdir(r"C:\OSGeo4W\apps\qgis\python\plugins"):
		sys.path.append(r"C:\OSGeo4W\apps\qgis\python\plugins")
		qgisprefix = r"C:\OSGeo4W\apps\qgis"
	elif os.path.isdir(r"C:\OSGeo4W\apps\qgis-ltr\python\plugins"):
		sys.path.append(r"C:\OSGeo4W\apps\qgis-ltr\python\plugins")
		qgisprefix = r"C:\OSGeo4W\apps\qgis-ltr"
	elif os.path.isdir(r"C:\OSGeo4W64\apps\qgis\python\plugins"):
		sys.path.append(r"C:\OSGeo4W64\apps\qgis\python\plugins")
		qgisprefix = r"C:\OSGeo4W64\apps\qgis"
	elif os.path.isdir(r"C:\OSGeo4W64\apps\qgis-ltr\python\plugins"):
		sys.path.append(r"C:\OSGeo4W64\apps\qgis-ltr\python\plugins")
		qgisprefix = r"C:\OSGeo4W64\apps\qgis-ltr"
	elif os.path.isdir(r"C:\Program Files (x86)"):
		is_osgeo = False
		qgis_folder = ""
		for folder in os.listdir(r"C:\Program Files (x86)"):
			if "QGIS" in folder.upper():
				qgis_folder = os.path.join(r"C:\Program Files (x86)",
										   folder)
				break
		if qgis_folder == "":
			for folder in os.listdir(r"C:\Program Files"):
				if "QGIS" in folder.upper():
					qgis_folder = os.path.join(r"C:\Program Files", folder)
					break
		if qgis_folder == "":
			print("Could not find QGIS installation.")
			print("Please email alexander.mcvittie@gmail.com for assistance")
			sys.exit(0)
	else:
		is_osgeo = False
		qgis_folder = ""
		for folder in os.listdir(r"C:\Program Files"):
			if "QGIS" in folder.upper():
				qgis_folder = os.path.join(r"C:\Program Files", folder)
				break
            
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
            qgisprefix = os.path.join(qgis_base, "apps", "qgis-ltr")
            sys.path.append(os.path.join(qgis_base, "apps", "qgis-ltr", "python", "plugins"))
        elif not is_osgeo:
            sys.path.append(os.path.join(qgis_base, "apps", "qgis", "python", "plugins"))
            qgisprefix = os.path.join(qgis_base, "apps", "qgis")
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
    #QgsApplication.setPrefixPath(qgisprefix, True)

#uninstallErrorHook() # Needed it for earlier versions of QGIS 
os.environ['QGIS_DEBUG'] = '-1'

#Package imports
import qgis
from qgis.core import *
from qgis.gui import *
from PyQt4.QtGui import QApplication

app = QApplication([])
QgsApplication.setPrefixPath(qgisprefix, True)
QgsApplication.initQgis()
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
    QgsApplication.setPrefixPath(get_qgisprefix(), True)
    iface = DummyInterface()
    plugin = processing.classFactory(iface)
    Processing.initialize()
    def getp(self):
        return g 
    def getqgs(self):
        return QgsApplication
    def exit(self):
        try:
            del app 
        except:
            print "Failed deleting app"
        try:
            del plugin
        except:
            print "Failed deleting plugin"
        try:
            del iface
        except:
            print "Failed deleting iface"
        try:
            del QgsApplication
        except:
            print "Failed deleting QgsApplication"
        try:
            del g 
        except:
            print "Failed deleting processing"
        try:
            del self
        except:
            print "Failed deleting Qprocess"
