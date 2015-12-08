from processing_obj import Qprocess


qgpy = Qprocess()
#Processing object
p = qgpy.getp()

#runalg: Any -> None
# Calls the runalg function from QGIS processing
def runalg(*arg):
	arguments = arg
	p.runalg(*arguments)

#alglist: Any -> None
# Calls the alglist function from QGIS processing
def alglist(*arg):
	arguments = arg
	p.alglist(*arguments)

#alghelp: String -> None
# Shows help on an algorithm passed in.
def alghelp(algorithm):
	p.alghelp(algorithm)

# algoptions: String -> None
#  Shows options available for a QGIS algorithm
def algoptions(algorithm):
	p.algoptions(algorithm)

# getobj
#  returns the specified QGIS object
def getobj(obj):
	return p.getobject(obj)

# values
#   Returns the values of the specified QGIS object
def values(*arg):
	return p.values(*arg)

# getfeatures: QGIS Layer object -> ??
#  Returns the features of the specified QGIS layer
def getfeatures(layer):
	return p.getfeatures(layer)

def uniquelabels(*arg):
	return p.uniquelabels(*arg)

# close: None -> None
# Closes the connection to QgsApplication. Haven't found this to be 
#  necessary during testing, but its good practice.
def close():
	# Exit applications
	QgsApplication.exitQgis()
	QApplication.exit()
