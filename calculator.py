# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 16:22:24 2026

@author: shrih
"""

#MOdular programming
#calculator
def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    if y==0:
        return "Error: Division by zero"
    return x/y