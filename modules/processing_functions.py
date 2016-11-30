#!/usr/bin/env python
from processing_obj import Qprocess
class CoreFunctions():
	def __init__(self, _p=None, _qgpy=None):
		self.p = _p
		self.gpy = _qgpy
	#runalg: Any -> None
	# Calls the runalg function from QGIS processing
	def runalg(self, *arg):
		arguments = arg
		self.p.runalg(*arguments)

	#alglist: Any -> None
	# Calls the alglist function from QGIS processing
	def alglist(self, *arg):
		arguments = arg
		self.p.alglist(*arguments)

	#alghelp: String -> None
	# Shows help on an algorithm passed in.
	def alghelp(self, algorithm):
		self.p.alghelp(algorithm)

	# algoptions: String -> None
	#  Shows options available for a QGIS algorithm
	def algoptions(self, algorithm):
		self.p.algoptions(algorithm)

	# getobj
	#  returns the specified QGIS object
	def getobj(self, obj):
		return self.p.getobject(obj)

	# values
	#   Returns the values of the specified QGIS object
	def values(self, *arg):
		return self.p.values(*arg)

	# getfeatures: QGIS Layer object -> ??
	#  Returns the features of the specified QGIS layer
	def getfeatures(self, layer):
		return self.p.getfeatures(layer)


	# uniquelabels: Any -> Any
	#  Returns all unique labels for layers in qpy instance 
	def uniquelabels(self, *arg):
		return self.p.uniquelabels(*arg)

	# close: None -> None
	# Closes the connection to QgsApplication. Haven't found this to be 
	#  necessary during testing, but its good practice.
	def close(self):
		self.qgpy.exit()
		del self.qgpy