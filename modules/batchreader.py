import re

def findvariables(batchpath):
	lov = dict()
	with open(batchpath,"r") as f:
		s = f.readline()
		while s != '' and s != '\n':
			