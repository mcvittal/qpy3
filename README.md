# qpy
A simpler way to use the PyQGIS libraries with standalone scripting.

If you're used to the simplicity of import arcpy from the ArcGIS suite, you'll soon discover that creating a standalone QGIS script is not nearly as easy as scripting with ArcPy. This (currently) small library attempts to mend that issue by creating all the necessary imports and setup that is needed. 

#Requirements
This package is developed on Arch Linux 64 bit, running the latest version of QGIS. It requires QGIS to be installed on the machine. The library assumes that you have python-qgis installed, and that the processing modules are located in /usr/share/qgis/python/plugins. It is written in Python 2.7. It is also tested on Windows 10 64 bit using the OSGeo4W shell.

This package appears to break when upgrading from QGIS 2.0.1 to 2.8.1. It is confirmed to work with 2.0, 2.12, and 2.14 in Linux Mint 17.2 and 17.3, as well as Arch Linux. I encourage people to try this out in other distros and operating systems. Open an issue and feel free to contribute if it does not run on your system.

It now requires GDAL to be installed as well. To install on Ubuntu based systems, run the following.

	sudo add-apt-repository ppa:ubuntugis/ubuntugis-unstable && sudo apt-get update && sudo apt-get install gdal-bin

Verify the installation by running

	ogrinfo

You should get something that looks like this:

	Usage: ogrinfo [--help-general] [-ro] [-q] [-where restricted_where]
		       [-spat xmin ymin xmax ymax] [-fid fid]
		       [-sql statement] [-al] [-so] [-fields={YES/NO}]
		       [-geom={YES/NO/SUMMARY}][--formats]
		       datasource_name [layer [layer ...]]

#Documentation

All documentation and code samples can be accessed on the [wiki](https://github.com/mcvittal/qpy/wiki).
