#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 07:27:18 2017

@author: nschue201
"""

import os
import json


class GeojsonParser(object):
    
    data_path = "./resources/data"
    geojson_path = "JeffreyBLewis/congressional-district-boundaries"
    
    def __init__(self):
        self.path = "%s/%s" % (self.data_path, self.geojson_path)
        self.geojson_files = [x for x in os.listdir(self.path)
                              if x.split(".")[-1] == "geojson"]
    
    def get_geojson_files(self):
        return self.geojson_files
    
    def get_path(self):
        return self.path
    
    def get_geojson(self, filepath):
        with open(filepath, "r") as f:
            return json.load(f)
    
    def get_features(self, geojson):
        return geojson.get('features')
    
    geojson = get_geojson(filepath)
    features = geojson.get('features')
    



with open("%s/%s" % (data_path, gejson_path, ), "r") as f:
    
    data = json.load(f)


with open("./resources/state_codes.json", "r") as f:
    state_codes = json.load(f)
    


for i in range(len(data["features"])):
    s = np.array(data["features"][i]["geometry"]["coordinates"]).shape
    data["features"][i]["geometry"]["coordinates"] = list(s)
    

for filename in os.listdir("%s/%s" % (data_path, geojson_path)):
    if filename.split(".")[-1] == "geojson":
        _path = "%s/%s/%s" % (data_path, geojson_path, filename)
        print(_path)
        with open(_path, "r") as f:
            geojson = json.load(f)
            break
        break
    break
