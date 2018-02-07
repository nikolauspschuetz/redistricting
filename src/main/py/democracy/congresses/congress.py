#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 17:54:17 2018

@author: nschue201
"""
from src.main.py.democracy.congresses.states.state import State

import pandas as pd
import numpy as np

class Congress(object):
    """Congress(object)
    A class to represent a session of congress.
    A Congress is added to a dictionary of congresses in the Government model, 
    as (key, val) of ({congress session number}, {Congress()})
    
    Parameters
    ----------
    cong : int value, default -1
        Session number of the congress object.
    
    Returns
    -------
    out : Congress
        Congress object of session number self.cong
    
    See also
    --------
    build()
    Government, State
    """
    
    states = dict()
    
    def __init__(self, cong=-1):
        self.cong = cong
    
    def add_state(self, d):
        """add_state(d)
        Add a state to the congress. The state is necessary for adding the
        district {d}.
            
        Parameters
        ----------
        d : District object
            A district object, from which the cong and state data are extracted
        
        Returns
        -------
        out : Congress
            Congress, with state added
        
        See also
        --------
        """
        cong, statename, statecd = d.get_cong(), d.get_statename(), d.get_statecd()
        print("adding state (%s) to cong (%d)" % (statecd, cong))
        self.states[statecd] = State(cong, statename, statecd)
    
    def has_state(self, statecd):
        """has_state(statecd)
        A helper function to determine if the Congress object's dictionary of
        (statecd, State) pairs does not include the statecd as a key.
        
        Parameters
        ----------
        statecd : str
            Two-letter state code
        
        Returns
        -------
        {True, False} : boolean
            true if statecd is in the congress' state keys
        
        See also
        --------
        """
        return statecd in self.states.keys()
    
    def get_state(self, statecd):
        return self.states.get(statecd)
    
    def add_district(self, d):
        
                # get the state and save it
        statecd = d.get_statecd()
        
        # check that it has the proper state!
        if not self.has_state(statecd):
            # pass the district into the state, it has metadata
            self.add_state(d)

        print("Adding district (%s) to cong (%d)" % (d.get_id(), d.get_cong()))
        self.states[statecd].add_district(d)
    
    def build(self):
        # build states
        for key in self.states.keys():
            self.states[key].build()
    
    def get_district(self, statecd, _id):
        return self.states.get(statecd).get_district(_id)
    
    def plot_districts(self, states=None):
        
        if states:
            if isinstance(states, str):
                pass
            elif isinstance(states, (list, np.array)):
                for st in states:
                    self.states[st].plot_districts()
        else:
            for st in self.states.keys():
                self.states[st].plot_districts()
    
    