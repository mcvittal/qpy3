#!/usr/bin/env python3

import sys 

sys.path.append("..")

from qpy3 import Qpy 

args = {}

args["INPUT"] = "demodata/gt30w020n90.tif"
args["Z_FACTOR"] = 0.75
args["AZIMUTH"] = 45
args["V_ANGLE"]=90
args["OUTPUT"]="demodata/gt30w020n90_hillshade.tif"

Qpy.processing.run("qgis:hillshade", args)