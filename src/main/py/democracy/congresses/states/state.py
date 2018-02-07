#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 18:00:19 2018

@author: nschue201
"""

from src.main.py.democracy.congresses.states.districts.district import District
from src.main.py.democracy.congresses.members import Member

class State(object):
    
    districts = dict()
    members = dict()
        
    def __init__(self, cong, statename, statecd):
        self.cong = cong
        self.statename = statename
        self.statecd = statecd
        # give it some dimensions
        self.dims = {
            "xys" : {
                "x" : {
                    "min" : None,
                    "max" : None,
                    },
                "y" : {
                    "min" : None,
                    "max" : None,
                    },
                },
            "coordinates" : {
                "x" : {
                    "min" : None,
                    "max" : None,
                    },
                "y" : {
                    "min" : None,
                    "max" : None,
                    },
                },
            }
    
    def get_cong(self):
        return self.cong
    
    def get_statename(self):
        return self.statename
    
    def get_statecd(self):
        return self.statecd
    
    def has_district(self, d):
        return d.get_district() in self.districts.keys()
    
    def add_district(self, d):
        print("Adding district (%s) to state (%s) in cong (%d)" % (d.get_id(), d.get_statecd(), d.get_cong()))
        self.districts[d.get_district()] = d
        self.add_member(d.get_member())
    
    def add_member(self, m):
        self.members[m.get_id()] = m
    
    def get_member(self, _id):
        print("""{self}\n{get_member}: {_id}""".format(
                {"self":self,
                 "get_member": self.get_member(_id),
                 "_id": self.get_member(_id).get_id()
                 }
                )
        )
        return self.members.get(_id)
    
        
    def get_dim(self, f, ix, kind="xys"):
        return -1
#        return min(self.get_dims())
    
    def get_dims(self, f, ix, kind="xys"):
        for key in self.districts.keys():
            yield self.districts[key].get_dim(f, ix, kind)
    
    def build(self):
        for key in self.districts.keys():
            self.districts[key].build()
        
#        self.build_dims()
#        self.build_I()
#    
#    def build_I(self):
#        self.build_corners()
        
    def build_dims(self):
        # for xys, coordinates
        for kind in self.dims.keys():
            # for x, y
            for xy in self.dims.get(kind).keys():
                # for min, max
                for f in self.dims[kind][xy].keys():
                    self.dims[kind][xy][f] = self.get_dim(f, xy, kind)
        
        
        # woot! figure out the space that the state fits in!
        
            
    def plot_districts(self, kind="xys"):
        for dkey in self.districts.keys():
            self.districts.get(dkey).plot_district()
    
    def to_string(self):
        
        return "State ({statecd}) in cong ({cong})".format(
                {"statecd" : self.statecd, "cong" : self.cong})
    