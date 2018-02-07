#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 17:58:30 2018

@author: nschue201
"""

import os
import json

#from src.main.py.democracy.congresses.states.districts import district

#from src.main.py.democracy.congresses.states.districts.district import District

RESOURCES_PATH = "./src/main/resources/"
DATA_PATH = RESOURCES_PATH + "data/"
JBL_PATH = "JeffreyBLewis/congressional-district-boundaries/"

JeffreyBLewis_data = DATA_PATH + JBL_PATH

#TODO: make this not an object but a collection of util functions
states = dict()
with open(RESOURCES_PATH + "state_codes.json", "r") as f:
    states = json.load(f)

state_cd_dict = dict(states.get("states"))
# reverse this for fun / later
state_name_dict = dict([(b,a) for a,b in state_cd_dict.items()])
        
def get_JeffreyBLewis_filenames(testing=False, testing_filepath=None, **kwargs):
    _testing = kwargs.get("testing", testing)
    testing_filepath = kwargs.get("testing_filepath", testing_filepath)
    files = os.listdir(JeffreyBLewis_data)
    if _testing:
        if testing_filepath:
            files = [x for x in files if x == testing_filepath]
        files = files[:1]
    for JeffreyBLewisFile in files:            
        if ".geojson" == JeffreyBLewisFile[-8:]:
            yield JeffreyBLewisFile

def get_JeffreyBLewis_json(JeffreyBLewis_filename):
    with open(JeffreyBLewis_data + JeffreyBLewis_filename, "r") as f:
        text = f.read()
    return json.loads(text)

def get_features(load):
    for feature in load.get("features"):
        yield feature

def parse_features(load):
    for feature in get_features(load):
        yield feature.get("geometry"), feature.get("properties")

def parse_properties(p):
    kv_pairs = (("district", int(p.get("district"))),
                ("statecd", state_cd_dict.get(p.get("statename"))),
                ("statename", p.get("statename")),
                ("startcong", int(p.get("startcong"))),
                ("endcong", int(p.get("endcong"))),
                ("member", p.get("member")),
                ("_id", p.get("id")),
                )
    for k,v in kv_pairs:
        yield k,v
    
def parse_districts(testing=False, testing_filepath=None):
    # get the filename (so you may pass it to the District)
    for JeffreyBLewis_filename in get_JeffreyBLewis_filenames(testing, testing_filepath):
        print("Parsing: " + JeffreyBLewis_filename)
        # get the json load from the file
        load = get_JeffreyBLewis_json(JeffreyBLewis_filename)
        # get and separate the geometry from the properties
        for (geometry, properties) in parse_features(load):
            dargs = {"geometry" : geometry,
                     "JeffreyBLewis_filename" : JeffreyBLewis_filename,
                     }
            # iter the parsed properties
            # "district", "statecd", "statename", "startcong", "endcong", "member", "id", 
            for key, val in parse_properties(properties):
                dargs[key] = val
            # message that this has worked
            msg = "Parsed district (%d) in state (%s) in congs (%d-%d)" % (
                    dargs.get("district"), dargs.get("statecd"),
                    dargs.get("startcong"), dargs.get("endcong"),
                    )
#                print(msg)
            # make a district for each session
            for cong in range(dargs.get("startcong"), dargs.get("endcong") + 1):
                dargs["cong"] = cong
                yield dargs