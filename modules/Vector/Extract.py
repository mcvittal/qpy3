class Extract():
    def __init__(self, processing, Processing):
        self.Processing = Processing
        self.processing = processing

    def Clip_analysis(self, in_features, clip_features, out_features, cluster_tolerance=None):
        pass

    def Select_analysis(self, in_features, out_feature_class, where_clause=None):
        pass

    def Split_analysis(self, in_featuures, split_features, split_field, out_workspace, cluster_tolerance=None):
        pass

    def SplitByAttributes_analysis(self, input_table, target_workspace, split_fields):
        pass

    def TableSelect_analysis(self, in_table, out_table, where_clause=None):
        pass