# qpy
A simpler way to use the PyQGIS libraries with standalone scripting

If you're used to the simplicity of import arcpy from the ArcGIS suite, you'll soon discover that creating a standalone QGIS script is not nearly as easy as scripting with ArcPy. This (currently) small library attempts to mend that issue by creating all the necessary imports and setup that is needed.

#Requirements
This package is developed on Linux Mint 17.2, running QGIS 2.0.1 Dufour. The library assumes that you have python-qgis installed, and that the processing modules are located in /usr/share/qgis/python/plugins. It is written in Python 2.7.

#Example usage
 >> import qpy
 >> qpy.alghelp("qgis:clip")
 ALGORITHM: Clip
 	INPUT <ParameterVector>
	OVERLAY <ParameterVector>
	OUTPUT <OutputVector>
	
	
More functions and built in help modules will be added in the future.
