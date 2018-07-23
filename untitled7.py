#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 31 13:36:15 2018

@author: aleksandradooley
"""

# This may not be how they wanted me to run it but it worked
d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
  # Your code here!
  print key + " " + d[key]
  
  
  
  
  
  
  
  
choices = ['pizza', 'pasta', 'salad', 'nachos']

print 'Your choices are:'
for index, item in enumerate(choices):
  print index + 1, item