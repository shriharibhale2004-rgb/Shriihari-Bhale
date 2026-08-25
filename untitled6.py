# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 16:23:51 2026

@author: shrih
"""
#Q1. Write a Python program to find the second largest number in a list without using built-in
#functions like max() or sort().


#Q.2 Write a function compress_string(s) that compresses repeated characters in a string using
#the count of repetitions. For example:
#ompress_string("aaabbccdaa") → "a3b2c2d1a2"
compress_string(" ")
count=0
while(num!=0):
    if num%10==digit:
        count=count+1 
    num=num//10
print(count) 
 

#Q3.Write a Python decorator called greet_decorator that adds the line "Hello!" before calling
#any function. Use it on a function say_name() that prints "My name is Python.". 
def test_function():
    def say_name():
        return "Hello"
    return say_name 
test=test_function()
test()

#Q.4 Create an iterator that returns the squares of numbers from 1 to 5 using a custom class. 



#Q.5 Write a code example showing the difference between shallow copy and deep copy using a
#list of lists. Modify one inner list after copying and show how each copy is affected.
import copy
list_a=[[1,2,3,4,5],[6,7,8,9,10]]
list_b= copy.copy(list_a)
list_a[0][0]=9
print(list_a)
print(list_b)
print("id of old list",id(list_a))
print("id of new list",id(list_b))


import copy
list_a=[[1,2,3,4,5],[6,7,8,9,10]]
list_b= copy.deepcopy(list_a)
list_a[0][0]=9
print(list_a)
print(list_b)
print("id of old list",id(list_a))
print("id of new list",id(list_b))



