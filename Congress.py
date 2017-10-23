#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:31:47 2017

@author: nschue201
"""

#import os
#import json

#import numpy as np

from utils import Utils, GeojsonParser

class Congress(object):
    
    DATA_PATH = "./resources/data/"
    is_print = True
    # fill this with districts
    districts = []
    sessions = {}
    
    gjp = GeojsonParser()
    
    def __init__(self, ncong=114, is_print=True):
        self.ncong = ncong
        self.is_print = is_print
    
    def fit(self):
        # make sessions
        self.make_sessions()
        # make the districts
        self.make_districts(self.is_print)
        # build sessions: sort the districts into state-session
        self.build_sessions()
    
    def make_districts(self, is_print=True):
        # work through the files
        for kwargs in self.gjp.parse_features(is_print):
            cong = kwargs.get("cong")
            feature = kwargs.get("feature")
            d = District(feature)
            d.fit(cong)
            self.districts.append(d)
    
    def build_sessions(self):
        for d in self.districts:
            self.add_district(d)
    
    def make_sessions(self):
        for cong in Utils.str_range("1", self.ncong):
            self.sessions[cong] = Session(cong)

    def add_district(self, d):
        # pass the district to the corret session
        self.sessions[d.cong].add_district(d)
        
    def add_session(self, cong):
        self.sessions[cong] = Session(cong)
    
    def has_session(self, cong):
        return cong in self.sessions.keys()            
    

class Session(object):
    
    states = {}
    
    def __init__(self, cong):
        self.cong = cong
    
    def has_state(self, statecd):
        return statecd in self.states.keys()
    
    def add_state(self, d):
        self.states[d.get_statecd()] = State(d)
    
    def add_district(self, d):
        # add the state if it needs it
        statecd = d.get_statecd()
        if self.has_state(statecd):
            self.states[statecd].add_district(d)
        else:
            self.add_state(d)
            self.states[statecd].add_district(d)
    
    def get_state(self, statecd):
        return self.states.get(statecd)

class State(object):
    
    districts = []
    
    def __init__(self, d):
        self.cong = d.cong
        self.statecd = d.get_statecd()
        self.feature = d.feature
        
    def fit(self, cong=None):
        pass
    
    def add_district(self, d):
        self.districts.append(d)
    
    def get_district(self, district):
        for d in self.districts:
            if d.get_district() == district:
                return d
    
    def has_district(self, d):
        for district in self.districts:
            if d.get_district_id() == district.get_district_id():
                return True
        return False


class District(object):
        
    def __init__(self, feature, cong=None):
        self.feature = feature
        self.geometry = self.feature.get("geometry")
        self.properties = self.feature.get("properties")
        self.coordinates = self.geometry.get('coordinates')
        if cong is not None:
            self.fit(cong)
    
    def fit(self, cong=None):
        if cong:
            self.cong = cong
        self.district_properties = DistrictProperties(self.feature.get("properties"))
        self.district_properties.fit(self.cong)
    
    def get_cong(self):
        return self.cong
    
    def get_keys(self):
        return {"cong":self.cong,
                "statecd":self.district_properties.statecd}
        self.properties
    
    def get_statecd(self):
        return self.district_properties.statecd
    
    def get_district(self, district):
        return self.district_properties.get_district()
    
    def get_district_id(self):
        return self.district_properties.district_id
    
class DistrictProperties(object):
    
    def __init__(self, properties):
        self.properties = properties
        # get data from properties
        self.district = self.properties.get("district")
        self.endcong = self.properties.get("endcong")
        self.district_id = self.properties.get("id") # id is python keyword
        self.startcong = self.properties.get("startcong")
        self.statename = self.properties.get("statename")
        self.statecd = Utils.get_statecd(self.statename)
        self.members = self.properties.get("member")
        
    def fit(self, cong):
        self.cong = cong
        self.member = Member(self.members)
        self.member.fit(self.cong)
    
    def get_district(self):
        return self.district

class Member(object):
    
    """name : string, name of congress member
    party : string, party of congress member
    """
    
    data = {}
    member_id = None
    name = None
    party = None
    
    def __init__(self, members):
        self.members = members
        
    def fit(self, cong):
        self.cong = cong
        member = self.members.get(self.cong)
        if isinstance(member, (dict)):
            self.member_id = list(member.keys())[0]
            self.data = member.get(self.member_id)
            self.name = self.data.get("name")
            self.party = self.data.get("party")