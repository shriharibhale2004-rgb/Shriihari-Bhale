# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 17:15:07 2026

@author: shrih
"""

a=10
b=0
result= a/b
# throws arithemeticexception/by zero
##
#zero division error
try:
    result =a/b
except ZeroDivisionError:
    print("cannot divide by zero")
#####
#index error
numbers=[1,2,3] 
print(numbers[5])    
try:
    print(numbers[5])
except IndexError:
    print("index out of range!") 
    
#handling exception without naming then

try:
    numerator=50
    denom=int(input("Enter the denominator"))
    quotient=(numerator/denom)
    print("DIvision performed successful")
except ValueError:
    print("only integer  should be entered")
except:
    print("OPPS... exception raise")   

#
try:
    numerator=50
    denom=int(input("Enter the denominator"))
    quotient=(numerator/denom)
    print("DIvision performed successful")
except ZeroDivisionError:
    print("donominator as Zero in not allowed")
except ValueError: 
    print("only INTEGERS should be entered")
else:
    print("the result of division operation is",quotient)   
       
try:
    numerator=50
    denom=int(input("Enter the denominator"))
    quotient=(numerator/denom)
    print("DIvision performed successful")
except ZeroDivisionError:
    print("donominator as Zero in not allowed")
except ValueError: 
    print("only INTEGERS should be entered")
else:
    print("the result of division operation is",quotient)   
finally:
    print("over and out")       
###
with open('c:/2-ad_python/pi_digits1.txt','r')as file:
     contents = file.read()
print(contents.rstrip()) 
###
try:
    with open('c:/2-ad_python/pi_digits1.txt','r')as file:
         contents = file.read()
except FileNotFoundError:
    print("file not found!")
  #  
with open('c:/2-ad_python/pi_digits.txt')as file:
     contents = file.read()
print(contents.rstrip()) 

#
try:
    with open('c:/2-ad_python/pi_digits1.txt','r')as file:
         contents = file.read()
    print(contents.rstrip())     
except PermissionError:
    print("you don't have permission to access this files!")
##
############
#AttributeError
obj = None
print(obj.some_attribute)
######
if obj is not None:
     print(obj.some_attribute)
else:
    print("object is None!")
###########
#MemoryError
huge_list = [1] * (10**10)
######### 
#handling using generator
def generate_numbers():
    for i in range(10**10):
        yield i
gen = generate_numbers()
print(next(gen))
###############
#recursive function
def recursive_function():
    return recursive_function()
recursive_function()
##############
import sys
sys.setrecursivrlimit(1000)
def safe_recursive_function(depth=0, max_depth=10):
    if depth >= max_depth:
        return "Done"
    return safe_recursive_function(depth + 1, max_depth)
print(safe_recursive_function())
############
#Intial Balance
balance = 500
def withdraw(amount):
    global balance #Allow modification of global balance
    try:
        #check if amount is valid number
        if not isinstance(amount, (int,float)):
            raise TypeError("Invalid amount type! Please enter a number.")
            
        #check amount is non negative
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        #check insufficient balance
        if amount > balance:
            raise ValueError("Insufficient balance!")
        #deduct amount
        balance -= amount
        print(f"withdrawal succussful! new balance: ${balance:.2f}")
    except TypeError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Trasaction failed: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
#test case
withdraw(100)
withdraw("fifty")
withdraw(500)
withdraw(-10)
########
#
def get_user_age():
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            raise ValueError("Age cannot be negative!")
        elif age < 18:
            raise ValueError("you must be at least 18 years old to proceed.")
        print("Access granted!")
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
get_user_age()
#########        
    

    
