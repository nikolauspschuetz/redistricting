#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 18:08:13 2018

@author: nschue201
"""

from src.main.py.democracy.congresses.congress import Congress
from src.main.py.utils.congress_utils import CongressUtils

class Government(object):
    
    congs = dict()
    
    def __init__(self):
        self.congress_utils = CongressUtils()
    
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
        for d in self.congress_utils.parse_districts():
            self.add_district(d)

