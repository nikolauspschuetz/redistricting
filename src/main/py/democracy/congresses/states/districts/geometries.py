#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 10:11:23 2018

@author: nschue201
"""

import numpy as np


from matplotlib import pyplot as plt

from src.main.py.democracy.congresses.states.districts.borders import Border, BorderSegment
from src.main.py.democracy.congresses.states.districts.line_segments import LineSegment, Point
from src.main.py.utils import congress_utils

class Geometry(object):
            
    def __init__(self, g, log_scale=(0,5)):
        self.border = Border(g)
        self.border.build()
        
        self.w = self.border.max_x - self.border.min_x
        self.h = self.border.max_y - self.border.min_y
        start, stop = log_scale
        num = stop - start + 1
        self.steps = np.logspace(start, stop, num, base=10, dtype=np.int64)
        self.line_segments = np.array(None)
        self.images = dict()
        
    def get_shape(self):
        return self.xyzs.shape
    
    def build(self, string=""):
        """
        build
        Builds list self.line_segments with built LineSegment objects
        """
        line_segments = list()
        
        for arr in self.border.xys:
            i = 1
            while (i < arr.shape[0]):
                # make points
                p0 = Point(*arr[i-1])
                p1 = Point(*arr[i])
                # make a line segment and append
                ls = LineSegment(p0, p1)
                ls.build()
                line_segments.append(ls)
                i+=1
        
        self.line_segments = line_segments
        #print("init-ing images for " + string)
        self.build_images()
            
    def iter_line_segments(self):
        for i, l in enumerate(self.line_segments):
            yield l
            
    def build_images(self):
        for step in self.steps:
            self.init_image(step)
            #self.build_image(step)
    
    def get_image(self, step=1):
        return self.images.get(step)

    def init_image(self, step):
        _m = np.round((self.h / step) + 1).astype(int)
        _n = np.round((self.w / step) + 1).astype(int)
        self.images[step] = np.zeros(shape=(_m, _n), dtype=np.int64)
    
    def get_m(self, step, y):
        image = self.images.get(step)
        return int(image.shape[0] - ((y - self.border.min_y) // step))
    
    def get_n(self, step, x):
        return int((x - self.border.min_x) // step)
    
    def get_y(self, step, m, l):
        image = self.images.get(step)
        return int(self.border.min_y + ((image.shape[0] - m) * step))
                
    def get_x(self, step, n, l):
        return int(self.border.min_x + (n * step))
    
    def get_xy(self, step, m, n, l):
        return self.get_x(step, n, l), self.get_y(step, m, l)

    def get_mn(self, step, x, y):
        return self.get_m(step, y), self.get_n(step, x)
    
    def iter_image_indices(self, step, l):
        image = self.get_image(step)
        """
        iterate through the image as follows:
            * find the m,n for where the line starts
            * yield this position
            
            then:
                * find the x of the next x-intercept
                * find the y of the next y-intercept
                * find the x at the y intercept
                * determine which intercept has a lesser x
                * find the m, n at that x
        """
        # the starting index for the line
        m, n = self.get_mn(step, l.min_x, l.get_y(l.min_x))
        yield m, n
        # the starting point of the line
        x, y = self.get_xy(step, m, n, l)
        # get this slope helper . . .
        slope = 1
        if l.m < 0:
            slope = -1
            
        # then walk down the line
        while (x <= l.max_x):
            x += step
            y += (step * slope)
            x_at_y = l.get_x(y)
            if x_at_y < x:
                x = x_at_y
            else:
                y = l.get_y(x)
            
            m, n = self.get_mn(step, x, y)
            if (m < image.shape[0]) and (n < image.shape[1]):
                yield (m, n)
            else:
                print(l.to_string(), l.m)
            
        # yield the last index if it's in the image
        if n < image.shape[1]:
            yield (m, n)
        else:
            print("skipped: m:%d, n:%d, x:%d, y:%d" % (int(m), int(n), int(x), int(y)))
    
    
    def build_image(self, step):
        for l in self.iter_line_segments():
            #print("build_image for line " + l.to_string())
            for m,n in self.iter_image_indices(step, l):
                try:
                    self.images[step][int(m), int(n)] = 1
                except:
                    tpl = (l.to_string(), int(step), m, n)
                    print("l=%s; step=%d, m=%d, n=%d" % tpl)
        """
        iterate through the line segments and fill in the image around each
        line segment
        
        for ls in self.iter_line_segments():
            x_offset, y_offset = ls.min_x, ls.min_y
            
            # get an iteration of all the points (m,n) that this line crosses
            for m,n in self.iter_image_intersections(step):
                # turn the point on
                self.image_data[m,n] = 1
        """                
        
    def plot_xys(self):
        for xy in self.xys:
            plt.plot(xy[:,0], xy[:,1])

    def plot_coordinates(self):
        for lonlats in self.coordinates:
            plt.plot(lonlats[:,0], lonlats[:,1])