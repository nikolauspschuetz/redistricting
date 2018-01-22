#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 17:59:36 2018

@author: nschue201
"""

class District(object):
    
    def __init__(self, geometry=None, district=None, statename=None,
                 startcong=None, cong=None, endcong=None, member=None, _id=None, **kwargs):
        
        self.geometry = kwargs.get("geometry", geometry)
        self.district = kwargs.get("district", district)
        self.statename = kwargs.get("statename", statename)
        self.startcong = kwargs.get("startcong", startcong)
        self.cong = kwargs.get("cong", cong)
        self.endcong = kwargs.get("endcong", endcong)
        self.member = kwargs.get("member", member)
        self._id = kwargs.get("_id", _id)
        
        # make sure to keep this updated
#        assert all([self.geometry, self.district, self.statename,
#                    self.startcong, self.cong, self.endcong,
#                    self.member, self._id,])
    
    def get_geometry(self):
        return self.geometry
    
    def get_district(self):
        return self.district
    
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
    
    def get__id(self):
        return self._id