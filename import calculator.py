# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 16:33:08 2026

@author: shrih
"""

import calculator

print(calculator.add(5,3))
print(calculator.sub(10,4))
print(calculator.mul(6,7))
print(calculator.div(8,2))
##
#main_script.py
from calculator import add
#Now you can use add() directly without prefix
result = add(10, 20)
print("Result:", result)
########
from calculator import sub
result = sub(10, 5)
print("Result:", result)
###########
from calculator import mul
result = mul(4, 7)
print("Result:", result)
##########
from calculator import div
result = div(10, 2)
print("Result:", result)

##
from calculator import add as summation

result= summation (15,20)
print("result:",result) 
#
from calculator import sub as summation

result= summation (15,20)
print("result:",result) 
#
from calculator import mul as summation

result= summation (15,20)
print("result:",result) 
#
from calculator import div as summation

result= summation (15,20)
print("result:",result) 
