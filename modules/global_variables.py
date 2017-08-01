#!/usr/bin/env python2

import os


overwriteOutput = True 

workspace = os.getcwd()

class Environment():
    def __init__(self):
        self._crs = 4326 # WGS 84 geographic coordinate system - standard 
        self._workspace = os.getcwd()
    def set_crs(self, crs_code):
        self._crs = crs_code 
    def get_crs(self):
        return self._crs 
	