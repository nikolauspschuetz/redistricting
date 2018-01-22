#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 17:58:30 2018

@author: nschue201
"""

import os
import json

from src.main.py.democracy.congresses.states.districts.district import District

RESOURCES_PATH = "./src/main/resources/"
DATA_PATH = "data/"
JBL_PATH = "JeffreyBLewis/congressional-district-boundaries/"

class CongressUtils(object):
    
    resources_path = ""
    data_path = ""
    JeffreyBLewis_data = ""
        
    def __init__(self, resources_path=RESOURCES_PATH, data_path=DATA_PATH, jbl_path=JBL_PATH):        
        self.resources_path = resources_path
        self.data_path = self.resources_path + data_path
        self.JeffreyBLewis_data = self.data_path + jbl_path
    
    def get_JeffreyBLewis_filenames(self):
        for JeffreyBLewisFile in os.listdir(self.JeffreyBLewis_data):
            if ".geojson" == JeffreyBLewisFile[-8:]:
                yield JeffreyBLewisFile
    
    def get_JeffreyBLewis_json(self, JeffreyBLewis_filename):
        with open(self.JeffreyBLewis_data + JeffreyBLewis_filename, "r") as f:
            text = f.read()
        return json.loads(text)
    
    def get_features(self, load):
        for feature in load.get("features"):
            yield feature
    
    def parse_features(self, load):
        for feature in self.get_features(load):
            yield feature.get("geometry"), feature.get("properties")
    
    def parse_properties(self, p):
        return int(p.get("district")), p.get("statename"), int(p.get("startcong")), int(p.get("endcong")), p.get("member"), p.get("id")
    
    def parse_districts(self):
        # get the filename (so you may pass it to the District)
        for JeffreyBLewis_filename in self.get_JeffreyBLewis_filenames():
            # get the json load from the file
            load = self.get_JeffreyBLewis_json(JeffreyBLewis_filename)
            # get and separate the geometry from the properties
            for (geometry, properties) in self.parse_features(load):
                # parse apart the properties
                district, statename, startcong, endcong, member, _id = self.parse_properties(properties)
                # make a district for each session
                for cong in range(startcong, endcong+1):
                    kwargs = {"geometry" : geometry,
                              "district" : district,
                              "statename" : statename,
                              "startcong" : startcong,
                              "cong" : cong,
                              "endcong" : endcong,
                              "member" : member,
                              "_id" : _id,                                    
                            }
                    yield District(**kwargs)