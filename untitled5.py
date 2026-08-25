# -*- coding: utf-8 -*-
"""
Created on Sun Feb  8 12:14:43 2026

@author: shrih
"""

with open('c:/2-ad_python/pi_digits.txt','r') as file:
    contents = file.read()
print(contents)
###########
#observe the extra line at the end of output
#####
#to avoid this rstrip() method is used
with open('c:/2-ad_python/pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())
#######
#
file_path = 'c:/2-ad_python/pi_digits.txt'

with open(file_path) as file_object:
    contents = file_object.read()

print(contents.rstrip())
#########
filename = 'c:/2-ad_python/pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line)
##########
filename = 'c:/2-ad_python/pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
lines
for line in lines:
    print(line.rstrip())
##########
#working with a file's contents
filename = 'c:/2-ad_python/pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
    for line in lines:
        pi_string = ''
        pi_string += line.rstrip()
        print(pi_string)
        print(len(pi_string))
###########
#writing to a file
filename = 'c:/2-ad_python/programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I am larning AI in  AIGenius ")
    
####
filename = 'c:/2-ad_python/programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I am learning AI in AIGenius")
 ##
file_name='c:/2-ad_python/programming.txt'
with open(filename,'w')as file_object:
     file_object.write("I am learning AI in AIGenius")
     file_object.write("i am feeling that i am genius")
##
file_name='c:/2-ad_python/programming.txt'
with open(filename,'w')as file_object:
     file_object.write("I am learning AI in AIGenius.\n")
     file_object.write("i am feeling that i am genius.\n")
##
filename='c:/2-ad_python/programming.txt'
with open(filename,'a')as file_object:
    #use a 'a' argument for open file for appending
    file_object.write("I also love finding meaning in large dataests.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
##error handling try except
filename='c:/2-ad_python/pi_digits.txt'
try:
    with open(filename, 'r',encoding="utf-8")as f:
        lines=f.readlines()
        for line in lines:
            print(line.rstrip())
except FileNotFoundError:
      print(f"Error: file '{filename}'not found.")
except PermissionError:
      print("error: permission denied while accessing the file.")  
###
text="मी AIGenius मध्ये skilling करत आहे आणि मला skilling करण्याचा आनंद होत आहे" 

with open("sample_utf8.txt",'w',encoding='utf-8')as f:
    f.write(text)
#
with open("sample_utf16.txt",'w',encoding='utf-8')as f:
    f.write(text)
#
with open("sample_utf8.txt",'w',encoding='utf-8')as f:
    f.write(text)
#
with open("sample_utf8.txt",'w',encoding='utf-8')as f:
    f.write(text)
    
###
  

        