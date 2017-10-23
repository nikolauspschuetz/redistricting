#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 07:27:18 2017

@author: nschue201
"""

import json
import os

class Utils(object):
    
    state_codes_path = "./resources/state_codes.json"
    with open(state_codes_path, "r") as f:
        states = json.load(f)
        state_names = dict((x,y) for x,y in states.get("states"))
        state_codes = dict((y,x) for x,y in states.get("states"))
    
    def str_range(start, stop):
        """helper function to make a range of str(int)"""
        for x in range(int(start), int(stop) + 1):
            yield str(x)
            
    def get_statecd(statename):
        return Utils.state_names.get(statename)
    
    def get_statename(statecd):
        return Utils.state_codes.get(statecd)



class GeojsonParser(object):
    
    data_path = "./resources/data"
    geojson_path = "JeffreyBLewis/congressional-district-boundaries"
    
    def __init__(self):
        self.path = "%s/%s" % (self.data_path, self.geojson_path)
        self.geojson_files = [x for x in os.listdir(self.path)
                              if x.split(".")[-1] == "geojson"]
    
    def get_geojson(self, filename):
        with open("%s/%s" % (self.path, filename), "r") as f:
            return json.load(f)
    
    def get_features(self, geojson):
        return geojson.get('features')
    
    def parse_features(self, is_print=True):
        
        for filename in self.geojson_files:
            if is_print:
                print("parsing %s" % filename)
            with open("%s/%s" % (self.path, filename), "r") as f:
                geojson = json.load(f)
            features = geojson.get("features")
            for feature in features:
                properties = feature.get("properties")
                startcong = properties.get("startcong")
                endcong = properties.get("endcong")
                for cong in Utils.str_range(startcong, endcong):
                    yield {"feature":feature,"cong":cong}
