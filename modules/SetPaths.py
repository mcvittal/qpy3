#!/usr/bin/env python3 

import os, sys, platform, getpass, subprocess

class SetPaths:
    def __init__(self):
        pass 
        self.addToPath()
    def isWindows(self):
        return "windows" in platform.platform().lower()
        
    def get_qgisprefix(self):
        if self.isWindows():
            #print("Initializing for a Windows system")
            qgis_folder = None
            is_osgeo = True
            
            if os.path.isdir(r"C:\OSGeo4W\apps\qgis\python\plugins"):
                return r"C:\OSGeo4W\apps\qgis"
            elif os.path.isdir(r"C:\OSGeo4W\apps\qgis-ltr\python\plugins"):
                return r"C:\OSGeo4W\apps\qgis-ltr"
            elif os.path.isdir(r"C:\OSGeo4W64\apps\qgis\python\plugins"):
                return r"C:\OSGeo4W64\apps\qgis"
            elif os.path.isdir(r"C:\OSGeo4W64\apps\qgis-ltr\python\plugins"):
                return r"C:\OSGeo4W64\apps\qgis-ltr"
            elif os.path.isdir(r"C:\Program Files (x86)"):
                is_osgeo = False
                qgis_folder = ""
                for folder in os.listdir(r"C:\Program Files (x86)"):
                    if "QGIS" in folder.upper():
                        return os.path.join(r"C:\Program Files (x86)", folder)
                if qgis_folder == "" or qgis_folder == None:
                    for folder in os.listdir(r"C:\Program Files"):
                        if "QGIS" in folder.upper():
                            return os.path.join(r"C:\Program Files", folder)
                if qgis_folder == "":
                    print("Could not find QGIS installation.")
                    print("Please email alexander.mcvittie@gmail.com for assistance")
                    sys.exit(0)
            else:
                is_osgeo = False
                qgis_folder = ""
                for folder in os.listdir(r"C:\Program Files"):
                    if "QGIS" in folder.upper():
                        return os.path.join(r"C:\Program Files", folder)
                    
                # Location of QGIS installation has been found. 
                # If it hasnt been found yet, it means it's not installed or they have
                # a custom setup. If the latter is the case, I'll need to add an
                # exception to the code.
                if qgis_folder == "":
                    print("Could not find QGIS installation.")
                    print("Please email alexander.mcvittie@gmail.com for assistance")
                    sys.exit(0)
                qgis_base = qgis_folder

                if not is_osgeo and "qgis-ltr" in os.listdir(os.path.join(qgis_base, "apps")):
                    return os.path.join(qgis_base, "apps", "qgis-ltr")
                elif not is_osgeo:
                    return os.path.join(qgis_base, "apps", "qgis")
        else:
            #print("Initializing for a UNIX system")
            return "/usr"
    
    # Add the processing plugin to the python path 
    def addToPath(self):
        if self.isWindows():
            print(self.get_qgisprefix())
            sys.path.insert(0, self.get_qgisprefix() + '/python/plugins')
            paths = ['C:/OSGEO4W64/apps/qgis/./python', 'C:/Users/USERNAME/AppData/Roaming/QGIS/QGIS3\\profiles\\default/python', 'C:/Users/USERNAME/AppData/Roaming/QGIS/QGIS3\\profiles\\default/python/plugins', 'C:/OSGEO4W64/apps/qgis/./python/plugins', 'C:\\OSGeo4W64\\bin\\python37.zip', 'C:\\OSGEO4W64\\apps\\Python37\\DLLs', 'C:\\OSGEO4W64\\apps\\Python37\\lib', 'C:\\OSGeo4W64\\bin', 'C:\\OSGEO4W64\\apps\\Python37', 'C:\\OSGEO4W64\\apps\\Python37\\lib\\site-packages', 'C:\\OSGEO4W64\\apps\\Python37\\lib\\site-packages\\win32', 'C:\\OSGEO4W64\\apps\\Python37\\lib\\site-packages\\win32\\lib', 'C:\\OSGEO4W64\\apps\\Python37\\lib\\site-packages\\Pythonwin', 'C:/Users/USERNAME/AppData/Roaming/QGIS/QGIS3\\profiles\\default/python']


            for path in paths:
                path = path.replace("USERNAME", getpass.getuser())
                if os.path.exists(path):
                    print("appending " + path)
                    sys.path.append(path)

        else:
            sys.path.append('/usr/share/qgis/python/plugins')
        