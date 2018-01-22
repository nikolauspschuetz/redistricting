#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 17:54:17 2018

@author: nschue201
"""
from src.main.py.democracy.congresses.states.state import State

class Congress(object):
    
    states = dict()
    
    def __init__(self, cong):
        self.cong = cong
    
    def add_state(self, d):
        cong, statename = d.get_cong(), d.get_statename()
        self.states[statename] = State(cong, statename)
    
    def has_state(self, statename):
        return statename in self.states.keys()
    
    def add_district(self, d):
        
                # get the state and save it
        statename = d.get_statename()
        
        # check that it has the proper state!
        if not self.has_state(statename):
            # pass the district into the state, it has metadata
            self.add_state(d)
        
        self.states[statename].add_district(d)