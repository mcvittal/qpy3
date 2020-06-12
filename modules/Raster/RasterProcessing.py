from qgis.core import QgsRasterLayer, QgsVectorLayer
import gdal, numpy
from osgeo import gdal_array

class RasterProcessingToolset():
    def __init__(self, processing, Processing):
        self.Processing = Processing
        self.processing = processing
        self.management = management(processing, Processing)

    def Clip_raster(self, in_raster, vector_path, out_path, target_crs=None, nodata=None, alpha_band=True):
        raster_layer = QgsRasterLayer(in_raster)
        vector_layer = QgsVectorLayer(vector_path)
        params = {}
        params["INPUT"] = raster_layer
        params["MASK"] = vector_layer
        params["CROP_TO_CUTLINE"] = True
        params["KEEP_RESOLUTION"] = True
        params["OUTPUT"] = out_path
        self.processing.run("gdal:cliprasterbymasklayer", params)

    def computeImageEdge(self, in_raster, out_vector_path, simplified=True):
        in_ds = gdal.Open(in_raster)
        band = in_ds.GetRasterBand(1)
        nd_value = 0
        array = in_ds.ReadAsArray()
        array[array == nd_value] = 0
        array[array != nd_value] = 1
        self.numpyArrayToRaster(array, in_ds.GetProjection(), in_ds.GetGeoTransform(), 0, "/tmp/binary.tif")
        simplified = QgsRasterLayer("/tmp/binary.tif")

        params = {}
        params["INPUT"] = simplified
        params["BAND"] = 1
        params["OUTPUT"] = out_vector_path
        self.processing.run("gdal:polygonize", params)

    def rasterToArray(self, in_raster):
        gdal.UseExceptions()
        gdal.PushErrorHandler('CPLQuietErrorHandler')
        ds = gdal.Open(in_raster).ReadAsArray()
        return ds

    def shiftRaster(self, in_raster, north=0, east=0, south=0,west=0):
        rast_src = gdal.Open(in_raster, 1)
        gt = rast_src.GetGeoTransform()
        gtl = list(gt)
        gtl[0] += east;
        gtl[0] -= west;
        gtl[3] += north;
        gtl[3] -= south;
        rast_src.SetGeoTransform(tuple(gtl))
        rast_src.SetNoDataValue(0)
        rast_src = None



    def rasterToCOG(self, in_raster, out_cog_path):
        # This requires GDAL 3 or higher. To install, run the following:
        # sudo add-apt-repository ppa:ubuntugis/ubuntugis-unstable
        if not (gdal.VersionInfo().startsWith("30")):
            print("Exporting to COG format is not supported in older GDAL versions. Please upgrade your install")
            return








    def numpyArrayToRaster(self, nparr, proj, geot, nodata_value, out_raster_path, dtype=None):
        gdal.AllRegister()
        np_dt = nparr.dtype
        if dtype == None:
            dtype = gdal_array.NumericTypeCodeToGDALTypeCode(np_dt)

        # Check if working with multiband raster
        if len(nparr.shape) == 3:
            n_bands = nparr.shape[0]
            for x in range(0, n_bands):
                driver = gdal.GetDriverByName('GTIFF')
                outDs = driver.Create(out_raster_path, nparr.shape[2], nparr.shape[1], n_bands, dtype,
                                      ['COMPRESS=LZW', 'TILED=YES', 'BLOCKXSIZE=128', 'BLOCKYSIZE=128'])
                outDs.GetRasterBand(x + 1).WriteArray(nparr[x])
                outDs.GetRasterBand(x + 1).SetNoDataValue(nodata_value)
                outDs.GetRasterBand(x + 1).FlushCache()
                outDs.SetProjection(proj)
                outDs.SetGeoTransform(geot)

                outDs = None
        else:
            driver = gdal.GetDriverByName('GTIFF')
            print(nparr.shape)
            outDs = driver.Create(out_raster_path, nparr.shape[1], nparr.shape[0], 1, dtype,
                                  ['COMPRESS=LZW', 'TILED=YES', 'BLOCKXSIZE=128', 'BLOCKYSIZE=128'])
            outDs.GetRasterBand(1).WriteArray(nparr)
            outDs.GetRasterBand(1).SetNoDataValue(nodata_value)
            outDs.GetRasterBand(1).FlushCache()
            outDs.SetProjection(proj)
            outDs.SetGeoTransform(geot)
            outDs = None
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
