#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 11:47:22 2018

@author: nschue201
"""

# -----------------------------------------------------------------------------
# From https://en.wikipedia.org/wiki/Minkowski–Bouligand_dimension:
#
# In fractal geometry, the Minkowski–Bouligand dimension, also known as
# Minkowski dimension or box-counting dimension, is a way of determining the
# fractal dimension of a set S in a Euclidean space Rn, or more generally in a
# metric space (X, d).
# -----------------------------------------------------------------------------
import scipy as sp
import numpy as np

from pyproj import Proj

#from src.main.py.democracy.congresses.states.districts.line_segments import Point

PROJ = Proj(proj='utm', zone="10S", ellps='WGS84')

def jitter(val=0):
    """
    jitter
    Add/subtract a random, miniscule, non-zero amount.
    This is useful when approximating the slope of a line; in many cases,
    a district boundary may be exactly vertical, causing divide-by-zero issues.
    """
    # avoid divide by zero
    return val + np.random.normal(scale=1e-16)

def get_xys(coordinates, dtype=np.int64):
    """
    get_xys
    Transform latitude-longitutde coordinate pairs into cartesian coordiantes.
    The transformation happens relative to the utm zone of Washington D.C.
    (Units are in meters.)
    """
    return np.array([[PROJ(lon, lat) for lon, lat in latlons] for latlons in coordinates], dtype=dtype)

def get_mins(xys):
    """
    get_mins
    Returns the minimum x and y coordinates in a list of xy coordinates.
    """
    return xys.min(axis=1)[0]

def get_maxs(xys):
    """
    get_maxs
    Returns the maximum x and y coordinates in a list of xy coordinates.
    """
    return xys.max(axis=1)[0]


#TODO: here, down
def iter_line_segment_points(g, ls, step=1):
    """
    iter_line_segment_points
    """
    pass
    
    

#def iter_point_line_segments(point, step=1):
#    """
#    this will return three line segments representing edges of the cell
#    to check for an intersection with the border's line segment
#    make points as fl
#    
#    p1 - l1 - p2 ___
#    |         |   |
#    l0        l2 step
#    |         |   |
#    p0 - l3 - p3 ___
#    | --step--|
#    
#    note: you don't need to check what would be l3;
#    if a line passes through "l3" it would also pass through
#    l0 or l2 (tests for intersection are inclusive inequalities)
#    
#    TODO: re-format documentation
#    """
#    p0 = Point(point.x, point.y)
#    p1 = Point(point.x, point.y + step)
#    p2 = Point(point.x + step, point.y + step)
#    p3 = Point(point.x + step, point.y)
#    
#    points = tuple([p0, p1, p2, p3])
#    
#    i = 1
#    
#    while i < len(points):
#        i+=1
#        yield points[i-1], points[i]
