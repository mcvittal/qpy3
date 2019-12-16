class RasterProcessingToolset():
    def __init__(self, processing, Processing):
        self.Processing = Processing
        self.processing = processing
        self.management = management(processing, Processing)

    def Clip_management(self, in_raster, rectangle, out_raster, in_template_dataset="#", nodata_value="#",
                        clipping_geometry="NONE", maintain_clipping_extent="NO_MAINTAIN_EXTENT"):
        pass

    def CompositeBands_management(self, in_rasters, out_raster):
        pass

    def ComputePansharpenWeights_management(self, in_raster, in_panchromatic_image, band_indexes=None):
        pass

    def CreateOrthoCorrectedRasterDataset_management(self, in_raster, out_raster_dataset, Ortho_type, constant_elevation,
                                                     in_DEM_raster=None, ZFactor=1, ZOffset=0, Geoid="NONE" ):
        pass

    def CreatePansharpenedRasterDataset_management(self, in_raster, red_channel, green_channel, blue_channel,  infrared_channel,
                                                   out_raster_dataset, in_panchromatic_image, pansharpening_type, red_weight=1,
                                                   green_weight=1, blue_weight=1, infrared_weight=1, sensor="UNKNOWN"):
        pass

    def ExtractSubDataset_management(self, in_raster, out_raster, subdataset_index=None):
        pass

    def RasterToDTED_management(self, in_raster, out_folder, dted_level, resampling_type="NEAREST"):
        pass

    def Resample_management(self, in_raster, out_raster, cell_size=None, resampling_type="NEAREST"):
        pass

    def SplitRaster_management(self, in_raster, out_folder, out_base_name, split_method, format, resampling_type,
                               num_rasters=None, tile_size=None, overlap=None, units=None, cell_size=None,
                               origin=None,split_polygon_feature_class=None, clip_type=None,
                               template_extent=None, nodata_value=None):
        pass

# why did esri set it up this way
# id like to make it better buuut they make it weird like this...
class management():
    def __init__(self, processing, Processing):
        self.processing = processing
        self.Processing = Processing

    def GenerateTableFromRasterFunction(self, raster_function, out_table, raster_function_arguments=None):
        pass
