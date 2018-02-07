#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 07:30:50 2018

@author: nschue201
"""

class Member(object):
    
    def __init__(self, m, cong):
        
        self.load = m.get(str(cong))
        if self.load == [] or self.load is None:
            self._id_key = "-1"
            self._id = -1
            self.details = dict()
            self.district = -1
            self.name = "NA"
            self.party = "NA"
            return
        
        self._id_key = list(self.load.keys())[0]
        self._id = int(self._id_key)
        self.details = self.load.get(self._id_key)
        self.district = int(self.details.get("district"))
        self.name = self.details.get("name")
        self.party = self.details.get("party")
    
    def get_load(self):
        return self.load
    
    def get_id_key(self):
        return self._id_key
    
    def get_id(self):
        return self._id
    
    def get_details(self):
        return self.details
    
    def get_district(self):
        return self.district
    
    def get_name(self):
        return self.name
    
    def get_party(self):
        return self.party

    def to_string(self):
        sargs = {"_self" : str(self),
                 "_id_key" : self._id_key,
                 "_id" : self._id,
                 "name" : self.name,
                 "party": self.party,
                 }
        txt = """Member {_self}
| _id_key: {_id_key}
| _id: {_id}
| district: {name}
| name: {party}
""".format(**sargs)
        return txt