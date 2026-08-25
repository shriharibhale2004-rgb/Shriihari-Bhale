# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 17:38:12 2026

@author: shrih
"""
# Advance Python
import pandas as pd 
f1=pd.read_csv('buzzers.csv')
f2=pd.read_csv('c:/2-ad_python/buzzers.csv')
#check working directory 
import os 
with open ('c:/2-ad_python/buzzers.csv') as raw_data:
    print(raw_data.read())
##read csv data as lists
import csv
with open('c:/2-ad_python/buzzers.csv') as raw_data:
    for line in csv.reader(raw_data):
        print(line)
##read csv as dictionaries
import csv
with open('buzzers.csv') as raw_data:
    for line in csv.reader(raw_data):
        print(line)
##
with open("buzzers.csv") as data:
    ignore=data.readline()
    for line in data:
        flights=line.strip( ).split(",")
        print(flights)    
###
file_name = "c:/2-ad_python/sample_utf8.txt"
try:
    with open(file_name, "r", encoding="utf-8")as f:
         data = f.read()
    print("file sccessfully")     
    print(data)
except FileNotFoundError:
    print(f"file not found: {file_name}")
except UnicodeDecodeError:
    print(f"file not decode'{file_name}' using utf-8" )     
## for latin
file_name = "c:/2-ad_python/sample_latin1.txt"
try:
    with open(file_name, "r", encoding="latin1")as f:
         data = f.read()
    print("file sccessfully")     
    print(data)
except FileNotFoundError:
    print(f"file not found: {file_name}")
except UnicodeDecodeError:
    print(f"file not decode'{file_name}' using latin1. " )     
##for ascii
file_name = "c:/2-ad_python/sample_ascii.txt"
try:
    with open(file_name, "r", encoding="ascii")as f:
         data = f.read()
    print("file sccessfully")     
    print(data)
except FileNotFoundError:
    print(f"file not found: {file_name}")
except UnicodeDecodeError:
    print(f"file not decode'{file_name}' using ascii. " )
##
#pre requisite decoders
def plus_one(number):
    number1=number+1 
    return number1
plus_one(5)     
# define function inside other function
def plus_one(number):
    
    def add_one(number):
        number1=number+1 
        return number1
    result = add_one(number)
    return result
plus_one(5)    
# pass function as argument
# to other function
def plus_one(number):
    number1 =number+1 
    return number1
def function_call(function):
    result=function(5)
    return result
function_call(plus_one)
##function returning other function
def hello_function():
    def say_hi():
        return "hi"
    return say_hi 
hello=hello_function()
hello()
###need for decoders
import time
def calc_square(numbers):
    start=time.time()
    result=[]
    for number in numbers:
        result.append(number*number)
    end=time.time()
    total_time=(end-start)*1000
    print(f"total time for execution square is {total_time}")
    return result

def calc_cube(numbers):
    start=time.time()
    result =[]
    for number in numbers:
        result.append(number*number*number)
    end=time.time()
    total_time=(end-start)*1000
    print(f"total time for execution cube is {total_time}")
    return result

array = range(1,1000000)
out_square=calc_square(array)
out_cube=calc_cube(array)    
###python decoder
#return it by adding some function
def say_hi():
    return "hello there"

def uppercase_decorater(function):
    def wrapper():
        func=function()
        make_uppercase=func.upper()
        return make_uppercase
    return wrapper
decorate=uppercase_decorater(say_hi)
decorate()    
##wit @ symbol for apply decorater

def uppercase_decorater(function):
    def wrapper():
        func=function()
        make_uppercase=func.upper()
        return make_uppercase
    return wrapper

@uppercase_decorater
def say_hi():
    return "hello there"
say_hi()
###
#applying multiple decorater in singile decorater
def split_string(function):
    def wrapper():
        func = function()
        splited_string = func.split()
        return splited_string
    return wrapper
def uppercase_decorater(function):
    def wrapper():
        func=function()
        make_uppercase=func.upper()
        return make_uppercase
    return wrapper
@split_string 
@uppercase_decorater
def say_hi():
    return "hello there"
say_hi()
###
import time
def time_it(func):
    #this is adecorater func that takes 
    #another function func as an argument
    def wrapper(*args,**kwargs):
        #*args and **kwargs allow wrapper
        #to accept all number of positional and key
        start = time.time()
        result = func(*args,**kwargs)
        end=time.time()
        print(func.__name__+"took"+str((end-start)*1000)+"mill sec")
        return result
    return wrapper
@time_it
def calc_square(numbers):
    result=[]
    for number in numbers:
        result.append(number*number)
array =range(1,1000000)
out_square = calc_square(array)
out_cube =calc_cube(array)
#