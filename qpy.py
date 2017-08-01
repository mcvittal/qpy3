#!/usr/bin/env python
from modules.processing_obj import Qprocess
from modules.processing_functions import CoreFunctions
from modules.layers import Layers
from modules.vector import VectorA

from modules.global_variables import Environment

'''

from modules.raster_toolsetA import RasterA

from modules.network_analysis import NetworkAnalyst
'''
# Initialize a Processing framework object, g
q = Qprocess()
g = q.getp()
iface = q.getdummy()

core = CoreFunctions(g, q)
vector_basic = VectorA(g)
layer = Layers(g)
environment = Environment()
qcore = layer.get_qgc()

#raster_basic = RasterA(g)
#raster_basic = RasterA(g)


