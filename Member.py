#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:41:16 2017

@author: nschue201
"""

class Member(object):
    
    """
    name : string, name of congress member
    party : string, party of congress member
    """
        
    def __init__(self, name, party):
        
        self.party = party
        self.name = name
        
    def get_name(self):
        return self.name
    
    def get_party(self):
        return self.party
        
    def set_name(self, name):
        self.name = name
        
    def set_party(self, party):
        self.party = party
