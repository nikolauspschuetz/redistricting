#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 17:16:31 2018

@author: nschue201
"""

import numpy as np

from pyproj import Proj

import src.main.py.utils.geometry_utils
from src.main.py.utils.geometry_utils import get_maxs, get_mins, get_xys, jitter

class Border(object):
    
    def __init__(self, g):
        self.coordinates = np.array(g.get("coordinates"))
        self.xys = get_xys(self.coordinates)
        self.borders = list()
        self.min_x, self.min_y = None, None
        self.max_x, self.max_y = None, None
    
    def build_image(self):
        origin = np.floor(self.min_x).astype(int), np.floor(self.min_y).astype(int), 
        m = np.ceil(self.max_y - self.min_y).astype(int)
        n = np.ceil(self.max_x - self.min_x).astype(int)
        self.image_data = np.zeros(shape=(m, n), dtype=int)
        
    def build(self):
        self.min_x, self.min_y = get_mins(self.xys)
        self.max_x, self.max_y = get_maxs(self.xys)
        
        for A in self.xys:
            tmp = list()
            i = 1
            while (i < A.shape[0]):
                p0 = A[i-1]
                p1 = A[i]
                tmp.append(BorderSegment((p0, p1)))
                i += 1
            self.borders.append(tmp)
        
        #build the image data
        
        self.build_image()
        

class BorderSegment(object):
        
    def __init__(self, l):
        # put the line from left to right
        self.l = sorted(l, key=lambda x: x[0])
        # extract points
        self.x1, self.x2 = self.l[0][0], self.l[1][0]
        self.y1, self.y2 = self.l[0][1], self.l[1][1]
        # calculate slope
        rise = self.y2 - self.y1
        # avoid divide by zero
        run = jitter(self.x2 - self.x1)
        self.m = None
        try:
            self.m = rise / run
        except:
            print(self.rise, self.run)
        # calculate b
        self.b = self.y1 - (self.m * self.x1)
        
        self.midpoint = (np.mean((self.x1, self.x2)),
                         np.mean((self.y1, self.y2)))
    
    def get_y(self, x):
        return self.m * x + self.b
    
    def get_x(self, y):
        return (y - self.b) / self.m
    
    def get_m(self):
        return self.m
    
    def get_b(self):
        return self.b
    
    def get_sorted_y(self):
        return tuple(sorted([self.y1, self.y2]))
    
    def intersects(self, l2):
        between_x = (self.x1 <= l2.midpoint[0] <= self.x2)
        # sorte the y
        _y1, _y2 = self.get_sorted_y()
        between_y = (_y1 <= l2.midpoint[1] <= _y2)
        
        if (between_x and between_y):
            return True
        
        return False
