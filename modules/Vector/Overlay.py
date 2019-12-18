from qgis.core import *

class Overlay():

    def Overlay():
        def __init__(self, Processing, processing):
            self.processing =processing
            self.Processing = Processing

    def Union(self, in_features, out_feature_class, join_attributes=None, cluster_tolerance=None, gaps=None):
        pass

    def Erase(self, in_features, erase_features, out_feature_class, cluster_tolerance=None):
        pass

    def Intersect(self, in_features, out_feature_class, join_attributes=None, cluster_tolerance=None, output_type=None):
        pass

    def identity(self, in_features, identity_features, out_feature_class, join_attributes=None, cluster_tolerance=None, relationship=None):
        pass

    def Spatial_Join(self, target_features, join_features, out_feature_class, join_operation=None, join_type=None, field_mapping=None, match_option=None, search_radius=None, distance_field_name=None):
        pass

    def Symmetrical_Difference(self, in_features, update_features, out_feature_class, join_attributes=None, cluster_tolerance=None):
        pass

    def Update(self, in_features, update_features, out_feature_class, keep_borders=None, cluster_tolerance=None):
        pass