from qgis.core import QgsVectorLayer, QgsExpression, QgsFeatureRequest, QgsVectorFileWriter

class Extract():
    def __init__(self, processing, Processing):
        self.Processing = Processing
        self.processing = processing

    def Clip_analysis(self, in_features, clip_features, out_features, cluster_tolerance=None):
        in_layer = QgsVectorLayer(in_features)
        clip_layer = QgsVectorLayer(clip_features)
        params = {}
        params["INPUT"] = in_layer
        params["MASK"] = clip_layer
        params["OUTPUT"] = out_features
        self.processing.run("gdal:clipvectorbypolygon", params)


    def Select_analysis(self, in_features, out_feature_class, where_clause=None):
        expr = QgsExpression(where_clause)
        in_layer = QgsVectorLayer(in_features)

        selection = in_layer.getFeatures(QgsFeatureRequest().setFilterExpression(where_clause))
        in_layer.selectByIds([s.id() for s in selection])

        QgsVectorFileWriter.writeAsVectorFormat(in_layer, out_feature_class,  "utf-8", in_layer.crs(), "ESRI Shapefile", onlySelected=True)


    def Split_analysis(self, in_features, split_features, split_field, out_workspace, cluster_tolerance=None):
        pass

    def SplitByAttributes_analysis(self, input_table, target_workspace, split_fields):
        pass

    def TableSelect_analysis(self, in_table, out_table, where_clause=None):
        pass