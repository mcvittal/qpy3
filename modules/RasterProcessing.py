class RasterProcessingToolset():
    def __init__(self, processing, Processing):
        self.Processing = Processing
        self.processing = processing

    def Clip_management(self, in_raster, rectangle, out_raster, in_template_dataset="#", nodata_value="#",
                        clipping_geometry="NONE", maintain_clipping_extent="NO_MAINTAIN_EXTENT"):
        pass