from qgis.core import QgsVectorLayer, QgsExpression, QgsFeatureRequest, QgsVectorFileWriter

class Extract():
    def __init__(self, processing, Processing):
        self.Processing = Processing
        self.processing = processing

    def clip_vector(self, in_features, clip_features, out_features):
        in_layer = QgsVectorLayer(in_features)
        clip_layer = QgsVectorLayer(clip_features)
        params = {}
        params["INPUT"] = in_layer
        params["MASK"] = clip_layer
        params["OUTPUT"] = out_features
        self.processing.run("gdal:clipvectorbypolygon", params)


    def select_vector(self, in_features, out_features, where_clause=None):
        expr = QgsExpression(where_clause)
        in_layer = QgsVectorLayer(in_features)

        selection = in_layer.getFeatures(QgsFeatureRequest().setFilterExpression(where_clause))
        in_layer.selectByIds([s.id() for s in selection])

        QgsVectorFileWriter.writeAsVectorFormat(in_layer, out_feature_class,  "utf-8", in_layer.crs(), "ESRI Shapefile", onlySelected=True)

