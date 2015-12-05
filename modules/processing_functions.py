from processing_obj import Qprocess

qgpy = Qprocess()

p = qgpy.getp()

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
