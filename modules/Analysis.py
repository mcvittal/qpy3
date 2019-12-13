from qgis.core import *

class Analysis():
    def __init__(self, processing, Processing):
        self.Processing = Processing
        self.processing = processing

    def Buffer(self, in_features, out_feature_class, buffer_distance_or_field):
        vlayer = QgsVectorLayer(in_features, "Input buffer feature", "ogr")
        params = {}
        params["INPUT"] = vlayer
        params["DISTANCE"] = buffer_distance_or_field
        params["DISSOLVE"] = True
        params["OUTPUT"] = out_feature_class
        self.processing.run("gdal:buffervectors", params)



