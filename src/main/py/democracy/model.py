#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 18:08:13 2018

@author: nschue201
"""

from src.main.py.democracy.congresses.congress import Congress
from src.main.py.democracy.congresses.states.districts.district import District
from src.main.py.utils import congress_utils as cu

class Government(object):
    
    congs = dict()
    testing = False
    
    def __init__(self, testing=False, testing_filepath="Tennessee_13_to_17.geojson", **kwargs):
        self.testing = kwargs.get("testing", testing)
        self.testing_filepath = kwargs.get("testing_filepath", testing_filepath)
    
    def add_cong(self, cong):
        self.congs[cong] = Congress(cong)
    
    def has_cong(self, cong):
        return cong in self.congs.keys()
    
    def get_cong(self, cong):
        return self.congs.get(cong)
    
    def add_district(self, d):
        #save which session of congress this district belongs to
        
        cong = d.get_cong()
        
        # if this session isn't there, add it first!
        if not self.has_cong(cong):
            self.add_cong(cong)
        
        # add the district to this session
        self.congs[cong].add_district(d)
        
    
    def build(self):
        """
        build:
        First, parse through all files and add the districts to self.
        This process creates an unbuilt collection of congresses.
        Second, call build() for each congress session. Note that congress
        sessions are the thighest-order object of this government model.
        """
        print("Building for %s" % "test" if self.testing else "prod")
        
        # for each 
        #TODO: fix congress utilss
        for dargs in cu.parse_districts(self.testing, self.testing_filepath):
            d = District(**dargs)
            print(d.to_string())
            self.add_district(d)
        
        for key in self.congs.keys():
            self.congs[key].build()
            