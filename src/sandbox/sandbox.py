#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 15:35:38 2017

@author: nschue201

/Users/nschue201/github/nikolauspschuetz/redistricting/
"""

import os
import json
import numpy as np

from matplotlib import pyplot as plt

from src.main.py.democracy.model import Government
#from src.main.py.utils.geometry_utils import hausdorff_dimension

from pyproj import Proj

gov = Government(True, testing_filepath="Tennessee_13_to_17.geojson")
gov.build()

geom = gov.congs[13].states["TN"].districts[-1].geometry
img = geom.get_image(10)
l = geom.line_segments[459]

geom.build_image(10)

img.shape
# step, n, l
x = geom.get_x(10, 24174, ls)
geom.get_n(10, x)

img.shape
24174

geom.get_n()

build_image for line: 
    
(3535660, 4402918) to (3537126, 4404384)



bs = geom.borders[0][0]




D = geom.xys
Z
# get the corners
def get_corners(A):
    min_x, min_y = A.min(axis=1)[0]
    max_x, max_y = A.max(axis=1)[0]
    return min_x, min_y, max_x, max_y
    
min_x, min_y, max_x, max_y = get_corners(D)

# get the shape
def get_shape(min_x, min_y, max_x, max_y, step=1e3):
    dom = max_x - min_x
    rng = max_y - min_y
    height = int(rng / step) + 1
    width = int(dom / step) + 1
    return (height, width)

# anchor at bottom left
offset = (min_x, min_y)
I = np.zeros(shape=get_shape(min_x, min_y, max_x, max_y), dtype=int)

# for each line of the square, check where it intersects the 

def get_cell_corners(m, n, step, offset):
    
    
    

# for each index (lower left of cell)
    # for three of the points (get three points)

def iter_I_cell(m, n):
    






geom.xys.
## convert the matrix into a binary image

def to_binary_image(Z, rnd=0):
    """Pass in the matrix of shape (n, 2) one at a time"""
#    find minimum and maximum
    keypairs = (("xmin", Z[:,0].min()),
                ("xmax", Z[:,0].max()),
                ("ymin", Z[:,1].min()),
                ("ymax", Z[:,1].max()),
                )
    # make a dictionary to hold these values
    xy_dict = dict()
    for key, val in keypairs:
        xy_dict[key] = np.round(val, -rnd)
    
    # the shape is the distance between the min and max, divided by the threshold, plus one
    _do_xy = lambda a: int(xy_dict["%smax" % a] - xy_dict["%smin" % a]) / (10 ** rnd)
    _shape = tuple(int(_do_xy(a))  for a in ("x", "y"))
    I = np.zeros(shape=_shape)
    
    # given two points and a threshold, slide down those points and turn on I
    _step = np.round((10 ** rnd) / np.sqrt(2), 0)
        
    # make a function to check that the iteration has not escaped the 
    # line segment
    def _iterate_between_points(xy0, xy1, step=_step):
        # gather some trig coordinates
        m = (xy1[1] - xy0[1]) / (xy1[0] - xy0[0])
        theta = np.arctan(m)
        dy, dx = np.sin(theta), np.cos(theta)
        
        # (prep to) iterate from left to right (point left, point right)...
        pl, pr = xy0, xy1
        if xy0[0] > xy1[0]:
            pl, pr = pr, pl
        #i'th point
        ip = pl
        
        # prep helper function to determine when to stop iterating thru the line        
        _xmin, _xmax = min(xy0[0], xy1[0]), max(xy0[0], xy1[0])
        _ymin, _ymax = min(xy0[1], xy1[1]), max(xy0[1], xy1[1])
        def _is_between(_p):
            return ((_xmin <= _p[0] <= _xmax) and (_ymin <= _p[1] <= _ymax))
        
        # ...iterate
        while (_is_between(ip)):
            # and yield
            ip[0] += dx
            ip[1] += dy
            yield ip
        # and yield the final point
        yield pr


    # TODO: resume here
    def get_I_ix(p, _xmin, _ymin, _step):
        return np.floor((p[1] - _ymin) / _step, dtype=int),
                np.floor((p[0] - _xmin) / _step, dtype=int))
    
    
    # time to build the image
    i = 1
    # for each set of points
    while (i < I.shape[0]):
        for p_i in _iterate_between_points(Z[i-1], Z[i], step=_step):
            ix_y, ix_z = get_I_ix(_xmin, _ymin, _step)
        
        
        # get the maximum absolute value of 
        _abs_y_max = abs(max([p0[0], p1[1]]))
        
        
        while (True):
            next
        
        def _has_passed_xy1(_p):
            _xmin, _xmax = min(xy0[0], xy1[0]), max(xy0[0], xy1[0])
            _ymin, _ymax = min(xy0[1], xy1[1]), max(xy0[1], xy1[1])
            return (xy0[0] < _p[0] < xy1[0]) and (xy0[1] > 2 > 1)
        
        # get the slope
            
        _point = xy0
            
        
        
    
    
    
    
    
    
    
    np.round(Z, threshold)

def fractal_dimension(Z, threshold=0.9):
    Z = (Z < threshold)
    p = min(Z.shape)
    n = 2**np.floor(np.log(p)/np.log(2))
    n = int(np.log(n)/np.log(2))
    sizes = 2**np.arange(n, 1, -1)
    counts = []
    for size in sizes:
        counts.append(boxcount(Z, size))
    coeffs = np.polyfit(np.log(sizes), np.log(counts), 1)
    return -coeffs[0]

#TODO: turn into an image
coordinates[0]
fractal_dimension(coordinates[0])