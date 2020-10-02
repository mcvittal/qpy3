from qgis.core import QgsRasterLayer, QgsVectorLayer
import gdal, numpy
from osgeo import gdal_array
import os
import uuid 
class RasterProcessingToolset():
    def __init__(self, processing, Processing):
        self.Processing = Processing
        self.processing = processing
        self.management = management(processing, Processing)

    def clip_raster(self, in_raster, in_vector, out_path):
        raster_layer = QgsRasterLayer(in_raster)
        vector_layer = QgsVectorLayer(in_vector)
        params = {}
        params["INPUT"] = raster_layer
        params["MASK"] = vector_layer
        params["CROP_TO_CUTLINE"] = True
        params["KEEP_RESOLUTION"] = True
        params["OUTPUT"] = out_path
        self.processing.run("gdal:cliprasterbymasklayer", params)

    def compute_edge_raster(self, in_raster, out_vector_path, nodata_value=0):
        in_ds = gdal.Open(in_raster)
        band = in_ds.GetRasterBand(1)
        nd_value = nodata_value
        array = in_ds.ReadAsArray()
        array[array == nd_value] = 0
        array[array != nd_value] = 1
        uuid_str = str(uuid.uuid1())
        filename = "/tmp/" + uuid_str + ".tif"
        self.numpyArrayToRaster(array, in_ds.GetProjection(), in_ds.GetGeoTransform(), 0, filename)
        simplified = QgsRasterLayer(filename)

        params = {}
        params["INPUT"] = simplified
        params["BAND"] = 1
        params["OUTPUT"] = out_vector_path
        self.processing.run("gdal:polygonize", params)
        try:
            os.remove(filename)
        except:
            pass 


    def raster_to_array(self, in_raster):
        gdal.UseExceptions()
        gdal.PushErrorHandler('CPLQuietErrorHandler')
        ds = gdal.Open(in_raster).ReadAsArray()
        return ds

    def shift_raster(self, in_raster, north=0, east=0, south=0,west=0):
        rast_src = gdal.Open(in_raster, 1)
        gt = rast_src.GetGeoTransform()
        gtl = list(gt)
        gtl[0] += east;
        gtl[0] -= west;
        gtl[3] += north;
        gtl[3] -= south;
        rast_src.SetGeoTransform(tuple(gtl))
        rast_src = None





'''
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
'''