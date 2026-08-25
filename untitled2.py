# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 17:20:05 2026

@author: shrih
"""

#python test
lstA=[1,2,3,4,5]
lstB=[3,4,6]
lst=lstA-lstB
print(find_diff(lstA,lstB))

print(lst)
#
#Question4
def is_palindrome(input):
    if input=="":
        return "You entered wrong input"
    else:
        string=input[::-1]
        if string==input:
            return True
        return False
    
print(is_palindrome("1221"))
#Question3

#Question2
num=[1,2,3,4,5,5]
count=0
while(num!=0):
     digit=num%10
     count=count+1 
     num=num//10
print(count)     
   

#QUESTION5
num=[1,2,3,4,5]
total=0
for i in range(len(num)):
    if num[i]%2!=0: 
        total=total+num[i]
print(total)  

   

