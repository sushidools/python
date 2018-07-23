#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 14:00:54 2018

@author: aleksandradooley
"""
# creating a function that concatenates strings
n = ["Michael", "Lieberman"]


def join_strings(words):
    result = ""
    for word in range(len(words)):
        result += word
    return result

print join_strings(n)


