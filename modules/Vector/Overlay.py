from qgis.core import *


class Overlay():

    def __init__(self, Processing, processing):
            self.processing = processing
            self.Processing = Processing


    def union_vector(self, in_features, out_features):
        parameter = {}
        parameter["A"] = QgsVectorLayer(in_features[0])
        parameter["B"] = QgsVectorLayer(in_features[1])
        parameter["SPLIT"] = True
        parameter["RESULT"] = out_features
        self.processing.run("saga:polygonunion", parameter)
