#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 18:00:19 2018

@author: nschue201
"""

from src.main.py.democracy.congresses.states.districts.district import District

class State(object):
    
    districts = dict()
    
    def __init__(self, cong, statename):
        self.cong = cong
        self.statename = statename
    
    def get_cong(self):
        return self.cong
    
    def get_statename(self):
        return self.statename
    
    def has_district(self, d):
        return d.get_district() in self.districts.keys()
    
    def add_district(self, d):
        self.districts[d.get_district()] = d