#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:54:14 2017

@author: nschue201
"""

class Term(object):
	
	def __init__(self, district, session, state):
		self.district = district
		self.session = session
		self.state = state

	def get_district(self):
		return self.district

	def get_session(self):
		return self.session

	def get_state(self):
		return self.state

	def set_district(self, district):
		self.district = district

	def set_session(self, session):
		self.session = session

	def set_state(self, state):
		self.state = state
