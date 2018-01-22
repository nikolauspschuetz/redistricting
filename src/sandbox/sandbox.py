#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 15:35:38 2017

@author: nschue201

for each file, load the file and parse it into?

"""

import os
import json
import numpy as np

#TODO: iterate throug files
#TODO: make/parse districts
#TODO: give districts proper info to sort them (congress, state, etc)
#TODO: have an add_district() for Congress()

#TODO: make a parseing pipeline

from src.main.py.democracy.model import Government

g = Government()
g.build()

dir(g)
cong = g.congs[1]

cong

cu = CongressUtils()

for d in cu.parse_districts():
    break

for JeffreyBLewis_filename in cu.get_JeffreyBLewis_filenames():
    load = cu.get_JeffreyBLewis_json(JeffreyBLewis_filename)
    break
    for (geometry, properties) in cu.parse_features(load):
        district, statename, startcong, endcong, member, _id = cu.parse_properties(properties)
        break
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
            

d = District(geometry, district, statename, startcong, cong, endcong, member, _id)


d.get_geometry()

for j in cu.get_JeffreyBLewis():
    print(j)
    break



with open("%s/%s/%s" % (data_path, geojson_path, filename), "r") as f:
    data = json.load(f)

#with open("./geojson-sample.json", "w") as f:
#    f.write(json.dumps(tmp))

with open("./src/main/resources/state_codes.json", "r") as f:
    state_codes = json.load(f)
    
    






from congress import Congress, District, DistrictProperties, Member, Session, State, Term
c = Congress()

from utils import Utils

Utils.state_names