# Qpy3


## Installation 

You can run the Docker compose file under the Dockerfiles/ folder in this repo to set up a minimal Ubuntu docker image that can run Qpy scripts. 


## Using Qpy 


To import, simply 

    import sys 
	sys.path.append("/path/to/qpy/folder")
	
	from qpy3 import Qpy 


To list all of QGIS' spatial algorithms that Qpy can access, you can run 


    qpy.alglist() 
	
	
and it will print to stdout all algorithms available. This method can also take in a single string argument to filter down the results containing only that string 


    qpy.alglist("buffer")
	

To get the specific information about one algorithm (Eg. GDAL:cliprasterbyextent), you can run 


    qpy.alghelp("GDAL:buffervectors") 
	
and it will return back what arguments it needs.

### Running a built-in algorithm 

To run any QGIS function as found in alglist, the Qpy.processing.run() function is used. It takes in two arguments - a string containing the lowercase name of the function (eg "gdal:buffervectors"), and a dictionary, where the keys are specified by the alghelp output, and the values are that input. 

Calling alghelp for GDAL:buffervectors returns back the following text:

    Buffer vectors (gdal:buffervectors)
    
    
    ----------------
    Input parameters
    ----------------
    
    INPUT: Input layer
    
    	Parameter type:	QgsProcessingParameterFeatureSource
    
    	Accepted data types:
    		- str: layer ID
    		- str: layer name
    		- str: layer source
    		- QgsProcessingFeatureSourceDefinition
    		- QgsProperty
    		- QgsVectorLayer
		
    GEOMETRY: Geometry column name

        Parameter type:	QgsProcessingParameterString

        Accepted data types:
            - str
            - QgsProperty

    DISTANCE: Buffer distance

        Parameter type:	QgsProcessingParameterDistance

        Accepted data types:
            - int
            - float
            - QgsProperty

    FIELD: Dissolve by attribute

        Parameter type:	QgsProcessingParameterField

        Accepted data types:
            - str
            - QgsProperty

    DISSOLVE: Dissolve all results

        Parameter type:	QgsProcessingParameterBoolean

        Accepted data types:
            - bool
            - int
            - str
            - QgsProperty

    EXPLODE_COLLECTIONS: Produce one feature for each geometry in any kind of geometry collection in the source file

        Parameter type:	QgsProcessingParameterBoolean

        Accepted data types:
            - bool
            - int
            - str
            - QgsProperty

    OPTIONS: Additional creation options

        Parameter type:	QgsProcessingParameterString

        Accepted data types:
            - str
            - QgsProperty

    OUTPUT: Buffer

        Parameter type:	QgsProcessingParameterVectorDestination

        Accepted data types:
            - str
            - QgsProperty
            - QgsProcessingOutputLayerDefinition

    ----------------
    Outputs
    ----------------

    OUTPUT:  <QgsProcessingOutputVectorLayer>
        Buffer
        
So to run GDAL buffervectors, you would need to construct a dictionary similar to this: 


    argdict = {}
    argdict["INPUT"] = "/path/to/input/vector.shp" # Any GDAL compatible vector dataset will be accepted 
    argdict["DISTANCE"] = 30 # This distance is in the units of the input dataset. If it is a geographic projection, this will be in degrees! 
    argdict["OUTPUT"] = "/path/to/output/vector.shp" # Any GDAL compatible vector dataset will be accepted 
    
    
Not all inputs are needed for QGIS algorithms. To run your algorithm, all you have to do is call this!

    Qpy.processing.run("gdal:buffervectors", argdict) 
    
    
    
## Built-in functions 

I did have some time to create some built-in functions that wrap some QGIS functionality during the development time of this Motivated Fridays project. 

### Vector functions
#### Vector buffering 

A wrapper for gdal:buffervectors. Buffers a vector dataset by a specified distance.

    Qpy.buffer_vectors(in_features="/path/to/input/vector.shp", out_features="/path/to/output/features.shp", buffer_distance_or_field=30)

#### Vector clipping

A wrapper for gdal:clipvectorbypolygon. Clips one vector dataset by the bounds of another.

in_features: The data you want clipped. Can be a point, line, or polygon.

clip_features: The data you want in_features clipped to. Must be a polygon.

    Qpy.clip_vector(in_features="/path/to/feature.shp", clip_features="/path/to/bounds/feature.shp", out_features="/path/to/output.shp")

#### Vector selection 

Allows you to grab a set of features from a feature set using an SQL expression. If you wanted cities with population > 10000 from a set of city points with a population field, you could do "'population' > 10000" as your where clause.

    Qpy.select_vector(in_features="/path/to/input.shp", out_features="/path/to/output.shp", where_clause="'population' > 10000")

#### Vector union 

Wrapper for saga:polygonunion. Returns back the union of two vector layers, given a list of two vector layer paths.

    Qpy.union_vector(in_features=["/path/to/first/input.shp", "/path/to/second/input.shp"], out_features="/path/to/output.shp")



### Raster functions 
#### Raster clipping 

Clips a raster given a polygon input. 

    Qpy.clip_raster(in_raster="/path/to/raster.tif", in_vector="/path/to/clipping/vector.shp", out_path="/path/to/clipped/raster.tif") 

#### Raster edge computation 

Creates a polygon of the outline of the raster. Can be useful for oddly clipped raster images. Nodata value is not always stored in the raster, so it may need to be passed in depending on the input. Defaults to 0 if it is not provided.

    Qpy.compute_edge_raster(in_raster="/path/to/raster.tif", out_vector_path="/path/to/raster/edge.shp", nodata_value=0)

#### Raster to numpy array 

Returns a numpy array of an input raster. 

    array = Qpy.raster_to_array(in_raster="/path/to/raster.tif")


#### Shift raster 

Shifts a raster north, south, east, or west by a specified amount. Does not warp the image, but rather shifts it by modifying its location information in the image header. This writes back to the same image you put in, so be cautious!

The following code will shift an image that is in a projected coordinate system 10 meters north and 30 meters east:

    Qpy.shift_raster(in_raster="/path/to/raster.tif", north=10, east=30)

The following code will shift an image that is in a projected coordinate system 15 meters south and 20 meters west:

    Qpy.shift_raster(in_raster="/path/to/raster.tif", south=15, west=20)
