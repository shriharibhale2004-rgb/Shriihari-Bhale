# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 18:01:06 2026

@author: shrih
"""

#iter tool

lst=[]
for num in range (0,20):
    lst.append(num)
print(lst)    
#
#code using list compression
lst=[num for num in range (0,20)]
print(lst)
##
names=["dada","mama","kaka"]
lst=[name.capitalize() for name in names]
print(lst)
## list comrehension with if statement
def is_even(num):
    return num%2==0
lst=[num for num in range(10) if is_even(num)]
print(lst)

def is_odd(num):
    return num%2!=0
lst=[num for num in range(9) if is_odd(num)]
print(lst)
###
evens =[num for num in range(10) if num%2==0]
print(evens)

odd = [num for num in range (15) if num%2!=0]
print(odd)
##
#LIST COMREHENSION FOR INSIDE FOR
lst=[f"(x):(y)"for x in range(3)for y in range(3)]
print(lst)
##
set_one={ x for x in range(3) } 
print(set_one)
##
dict={x:x*x for x in range(3)}
print(dict)
###
#generator expression
sum_evens = sum(num for num in range (10) if num %2==0)
sum_evens
print(sum_evens)

sum_odd = sum(num for num in range (10) if num %2!=0)
sum_odd
print(sum_odd)
#generator
gen=(x for x in range(3))
print(gen)
for num in gen:
    print(num)
###
gen=(x for x in range (3))
next(gen)
##
#function with returns multiple values
def range_even(end):
    for num in range(0,end,2):
        yield num
range_even(6)
for num in range_even(6):
    print(num)   
#
gen=range_even(6)
next(gen)
next(gen)     
#let us hid password entered on screen
#chaining generator
def length(itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in itr:
        yield ele*'*'
password=["not-good","give-m pass", "00100-100"]
for password in hide(length(password)):
    print(password) 
#enumerate
#printing list with index
lst=["milk","egg","bread"]
for index in range(len(lst)):
    print(f"{index+1} {lst[index]}")

#code can be implement using enumerate
lst=["milk","egg","bread"]
for index,item in enumerate(lst,start=1):
    print(f"{index} {item}")

#use zip function
name=["dada","mama","kaka"]
info={9850,7890,9785}
for nm,inf in zip(name,info):
    print(nm,inf)  
##use o fzip function with match list
name=["dada","mama","kaka","baba"]
info={9850,7890,9785}
for nm,inf in zip(name,info):
    print(nm,inf)  
##
#zip longest
from itertools import zip_longest
name=["dada","mama","kaka","baba"]
info={9850,7890,9785}
for nm,inf in zip_longest(name,info):
    print(nm,inf)  
#use of fill value insted none
from itertools import zip_longest
name=["dada","mama","kaka","baba"]
info={9850,7890,9785}
for nm,inf in zip_longest(name,info,fillvalue=0):
    print(nm,inf) 
##use of all() if value are 
#true  then it all produce output
lst=[2,3,-6,8,9]
if all(lst):
    print("all values are true")
else:
    print("ther are null values")    
 
lst=[2,3,0,8,9]
if all(lst):
    print("all values are true")
else:
    print("ther are null values")    
##use of any if one zero value
lst=[0,0,0,-8,0]
if any(lst):
   print("it has some non zero value")
else:
   print("all values are null in list")    
##
lst=[0,0,0,0,0]
if any(lst):
   print("it has some non zero value")
else:
   print("all values are null in list")    
###COUNT()
from itertools import count
counter=count()
print(next(counter))
print(next(counter))
print(next(counter))
##
from itertools import count
counter=count(counts+1)
print(next(counter))
print(next(counter))
print(next(counter))

##cycle()
import itertools

instruction=("eat","code","sleep") 
for instruction in itertools.cycle(instruction):
    print(instruction)
#repeat()
from itertools import repeat
for msg in repeat("keep","patience",times=2):
    print(msg) 
    
##combination()
from itertools import combinations
player=["john","jami","janardhan"]
for i in combinations(player,2):
    print(i) 
    
##permutations
from itertools import permutations
player=["John","Jani","Janardhan"]
for seat in permutations(player,2):
    print(seat) 
##
#product()
from itertools import product
team_a=['rohit','panday','bumrah']
team_b=['virat','manish','sami']
for pair in product(team_a,team_b):
    print(pair)    
#
age=[27,17,21,19]
adult=filter(lambda age:age>=18,age) 
print([age for age in adult])   
##shallow copy
import copy
list_a=[1,2,3,4,5]
list_b=copy.copy(list_a)

list_b[0]=-10

print("old list:",list_a )
print("id of old list", id(list_a))

print("old list:",list_b )
print("id of old list", id(list_b))
#for nested list

import copy
list_a=[[1,2,3,4,5],[6,7,8,9,10]]
list_b= copy.copy(list_a)
#affect the other!
list_a[0][0]=-10
print(list_a)
print(list_b)

print("id of old list",id(list_a))
print("id of new list",id(list_b))
##
import copy
list_a=[[1,2,3,4,5],[6,7,8,9,10]]
list_b= copy.deepcopy(list_a)
#affect the other!
list_a[0][0]=-10
print(list_a)
print(list_b)

print("id of old list",id(list_a))
print("id of new list",id(list_b))
