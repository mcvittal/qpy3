from qgis.core import QgsVectorLayer

from modules.Vector.Extract import Extract

# Inherit the Extract subclass of Analysis
class Analysis(Extract):
    def __init__(self, processing, Processing):
        self.Processing = Processing
        self.processing = processing

    def Buffer(self, in_features, out_feature_class, buffer_distance_or_field, line_side="FULL",
               line_end_type="ROUND", dissolve_option="NONE", dissolve_field=None, method="PLANAR"):
        vlayer = QgsVectorLayer(in_features, "Input buffer feature", "ogr")
        params = {}
        params["INPUT"] = vlayer
        params["DISTANCE"] = buffer_distance_or_field
        params["DISSOLVE"] = True
        params["OUTPUT"] = out_feature_class
        self.processing.run("gdal:buffervectors", params)

    def CreateThiessenPolygons_analysis(self, in_features, out_feature_class, fields_to_copy="ONLY_FID"):
        pass

    def GenerateNearTable_analysis(self, in_features, near_features, out_table, search_radius=None, location=None, angle=None,
                          closest=None, closest_count=None,method=None):
        pass

    def GraphicBuffer_analysis(self, in_features, out_feature_class, buffer_distance_or_field, line_caps="SQUARE",
                               line_joins="MITER", miter_limit=None, max_deviation=None):
        pass

    def MultipleRingBuffer_analysis(self, input_features, output_feature_class, distances, buffer_unit="DEFAULT",
                                    field_name="distance", dissolve_option="ALL", outside_polygons_only="FULL" ):
        pass

    def Near_analysis(self, in_features, near_features, search_radius=None, location="NO_LOCATION", angle="NO_ANGLE",
                      method="PLANAR"):
        pass

    def PointDistance_analysis (self, in_features, near_features, out_table, search_radius="ALL"):
        pass
    
    def PolygonNeighbors_analysis(self, in_features, out_table, in_fields=None,area_overlap="NO_AREA_OVERLAP",
                                 both_sides="BOTH_SIDES", cluster_tolerance=None, out_linear_units=None,
                                 out_area_units=None):
        pass




