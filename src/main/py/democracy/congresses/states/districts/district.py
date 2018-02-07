#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 17:59:36 2018

@author: nschue201
"""

from src.main.py.democracy.congresses.members import Member
from src.main.py.democracy.congresses.states.districts.geometries import Geometry

from matplotlib import pyplot as plt

class District(object):
    
    def __init__(self, geometry=None, district=None, statename=None,
                 statecd=None, startcong=None, cong=None, endcong=None,
                 member=None, _id=None, JeffreyBLewis_filename=None,
                 **kwargs):
        
        self.geometry = Geometry(kwargs.get("geometry", geometry))
        self.district = kwargs.get("district", district)
        self.statename = kwargs.get("statename", statename)
        self.statecd = kwargs.get("statecd", statecd)
        self.startcong = kwargs.get("startcong", startcong)
        self.cong = kwargs.get("cong", cong)
        self.endcong = kwargs.get("endcong", endcong)
        self.members = kwargs.get("member", member)
        self.member = Member(self.members, self.cong)
        self._id = kwargs.get("_id", _id)
        self.JeffreyBLewis_filename = kwargs.get("JeffreyBLewis_filename",
                                                 JeffreyBLewis_filename)
        
        # make sure to keep this updated
#        assert all([self.geometry, self.district, self.statename,
#                    self.startcong, self.cong, self.endcong,
#                    self.member, self._id,])
    
    def get_geometry(self):
        return self.geometry
    
    def get_district(self):
        return self.district
    
    def get_statecd(self):
        return self.statecd
    
    def get_statename(self):
        return self.statename
    
    def get_startcong(self):
        return self.startcong
    
    def get_cong(self):
        return self.cong
    
    def get_endcong(self):
        return self.endcong
    
    def get_member(self):
        return self.member
    
    def get_id(self):
        return self._id
    
    def get_JeffreyBLewis_filename(self):
        return self.JeffreyBLewis_filename
    
    def plot_district(self, kind="xy"):
        if kind == "xy":
            self.geometry.plot_xy()
            
        elif kind == "coordinates":
            self.geometry.plot_coordinates()
    
    def get_dim(self, f, ix, kind="xy"):
        return self.geometry.get_dim(f, ix, kind)
    
    def build(self):
        self.geometry.build(self.to_string())
#        self.build_corners()
    
    #TODO: resume here
#    def build_corners(self):
#        
#        self.min_x, self.min_y, self.max_x, self.max_y = self.get_corners()
#        self.min
    
    def to_string(self):
        sargs = {"_self" : str(self),
                 "district" : self.district,
                 "statename" : self.statename,
                 "statecd" : self.statecd,
                 "startcong" : self.startcong,
                 "cong" : self.cong,
                 "endcong" : self.endcong,
                 "member": self.member,
                 "_id" : self._id,
                 "JeffreyBLewis_filename" : self.JeffreyBLewis_filename,
                 }
        
        txt = """District {_self}
| district: {district}
| statename: {statename}
| statecd: {statecd}
| startcong: {startcong}
| cong: {cong}
| endcong: {endcong}
| _id: {_id}
| JeffreyBLewis_filename: {JeffreyBLewis_filename}
""".format(**sargs)

        return txt