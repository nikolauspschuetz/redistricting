#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 13:39:28 2018

@author: nschue201
"""
import numpy as np

import src.main.py.utils.geometry_utils
from src.main.py.utils.geometry_utils import jitter

class LineSegment(object):
    """LineSegment
    
    initialize with two Point objects p0, p1
    """
    
    def __init__(self, p0, p1):
        self.p0 = p0
        self.p1 = p1
        
    def build(self):
        """
        build
        Calculates the slope-intercept form of the line and adds metadata
        (min/max values of x/y, height h and width w)
        """
        # get the slope and intercept
        rise = self.p0.y - self.p1.y
        run = jitter(self.p0.y - self.p1.y)
        # apply algebra
        self.m = rise / run
        self.b = self.p0.y - (self.m * self.p0.x)
        # get theta
        self.theta = np.arctan(self.m)
        self.dx, self.dy = np.cos(self.theta), np.sin(self.theta)
        # get metadata
        self.min_x, self.max_x = [self.get_dim(f, "x") for f in (min, max)]
        self.min_y, self.max_y = [self.get_dim(f, "x") for f in (min, max)]
        self.h, self.w = (self.max_y - self.min_y), (self.max_x - self.min_x)
    
    def get_dim(self, f, axis="x"):
        #TODO: document
        if axis == "x":
            return f([self.p0.x, self.p1.x])
        
        return f([self.p0.y, self.p1.y])
    
    def get_y(self, x):
        #TODO: document
        return (self.m * x) + self.b
    
    def get_x(self, y):
        #TODO: document
        return (y - self.b) / self.m

    
    def is_between(self, val, axis="x"):
        """is_between(val, axis="x")
        Essential function for testing intersection of two LineSegment objects.
        Tests that the value x or y is between the minimum and maximum x or y
        
        Parameters
        ----------
        val : int
            the value by which to test for betweenness
            
        axis : str, {"x", "y"}
            the axis by wich to test for betweenness
            
        
        Returns
        -------
        true, false : boolean
            True if the value is within the min and max values on it's respective
            axis.
        
        See also
        --------
        self.intersects(ls)
        """
        if axis == "x":
            return (self.min_x <= val <= self.max_x)
        else:
            return (self.min_y <= val <= self.max_y)
        
    def get_theta(self):
        np.arctan()
        
    def intersects(self, ls):
        """intersects(ls)
        A Congress is added to a dictionary of congresses in the Government model, 
        as (key, val) of ({congress session number}, {Congress()})
        
        Parameters
        ----------
        ls : LineSegment
            The lineSegment with which this LineSegment (self) will be
            tested for intersection
        
        Returns
        -------
        true, false : boolean
            True if the LineSegment ls intersects with self
        
        See also
        --------
        NA
        """
        x = (ls.b - self.b) / (self.m - ls.m)
        y = self.get_y(x)
        
        zp = zip((x, y), ("x", "y"))
        
        return all([self.is_between(val, axis) for val, axis in zp])
    
    
    def walk(self, step):
        """walk down the line"""
        
        def get_deltas():
            pass
        
        dx, dy = get_deltas()
        
        def ordered_points():
            if self.p0.x == self.min_x:
                return self.p0, self.p1
            return self.p1, self.p0
            
        p, p1 = ordered_points()
        x = p.get_x()
        
    def to_string(self):
        x0 = self.min_x
        y0 = self.get_y(x0)
        x1 = self.max_x
        y1 = self.get_y(x1)
        vals = (x0, y0, x1, y1)
        return "(%d, %d) to (%d, %d)" % vals


class Point(object):
    
    """
    Point
    Essentially a helper class to organize x,y points within Geometry and
    LineSegment classes, for example.
    """
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y