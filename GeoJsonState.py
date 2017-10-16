#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 15:35:38 2017

@author: nschue201
"""

import os
import json

data_path = "./resources/data"
geojson_path = "JeffreyBLewis/congressional-district-boundaries"

with open("%s/%s" % (path,"Alabama_103_to_107.geojson"), "r") as f:
    data = json.load(f)


json.dumps(data)

features.geometry.coordinates


data.get('features')


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


with open("./resources/state_codes.json", "r") as f:
    state_codes = json.load(f)