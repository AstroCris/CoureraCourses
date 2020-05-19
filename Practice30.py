# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 16:19:11 2019

@author: astro
"""

from Practice22 import cleanEnds
import random

def pickWD():
    with open('sowpods.txt','r') as open_file:    
        f = open_file.readlines()
    f=cleanEnds(f)
    wd= f[random.randint(1,len(f))]
    return wd
