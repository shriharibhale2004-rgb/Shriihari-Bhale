# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 16:41:29 2026

@author: shrih
"""
#intall regex
import re
# basic character
#1..(dot) matches any charcter except newline

print(re.findall(r"a.c","abc aac acc adc a-c"))
#
print(re.findall(r"a.c","abc aac acc adc a-d"))
#not match a-d

#a= match the letter 'a'
#.=match any one character (except newline \n)
#c= match the letter 'c'
#so overall its looking for three character strings where:
#first letter is'a'
#last letter is'c'
#the middle can be any character
#b,a,c,-,d
#abc a+any char b+c 

#2.\d-digit
print(re.findall(r"\d+", "123 abc 456"))   
#pattern: \d+
#breakdown:
#\d matches any digits from 0  to 9
#the plus quantifier means "one or more" of the preceding element
#in this case digits so \d+ matches one or more digits in a row 
#this pATTERN   wil  matches
#sequence
#123 yes three digits its matches\d+
#abc no no digits here
#456 yes three digits so it match\d+

#####################
#3. \D = not digit
print(re.findall(r"\D+", "123 abc 456"))   
#[' abc ']

#\D= matches any non digits
#+  #the plus quantifier means "one or more" of the preceding element
#in this case digits so \d+ matches one or more digits in a row 
#sequence
#123 no does not match
#abc yes non digit
#456 no does not match

#4.  \w = word character (alpha numeric +)
print(re.findall(r"\w+", "a_b 123 @!"))
#ot ['a_b', '123']
#all sequence of letters, digits or underscore

#############
#5 \W = not a word  char
print(re.findall(r"\W+","a_b 123 @!#"))
#ot [' ', ' @!#']

#6. \s= whitespaces
print(re.findall(r"\s+","a b\tc\nd"))
#ot [' ', '\t', '\n']
#matches any whitespace character including

#7. \S non white spaces
print(re.findall(r"\S+","a b\tc\nd "))
#ot ['a', 'b', 'c', 'd']

##################
# Anchors
#1. ^(carret) match start of string
print(re.findall(r"^Hello","Hello world\nHello Python"))
#ot ['Hello']
print(re.findall(r"^world","world hello\nHello Python"))
#########

#2. $(dollar) matches end of string
print(re.findall(r"world$","Hello world"))
#ot ['world']

#############
#3 \b matches:
#before the firstbletter /number of a word
text="Hello world! welcome to regex."
matches= re.findall(r"\b\w+\b",text)
print(matches)

text="I love python and python is great!"
matches= re.findall (r"\bpython\b",text)
print(matches)    
#the \b on both ends ensures that it matches whole words (letters and digits)
text="I like python and java"
matches=re.findall(r"\bpython\b",text)
print(matches)
############

#4. \B non word boundary
text="Educational"
matches=re.findall(r"\Bcat\B",text)
print(matches)
#########################

#Quantifier
#1. *(asterisk) 0 or more of the preceding character
print(re.findall(r"ab*c","ac abc abbc abbbc"))
#ot ['ac', 'abc', 'abbc', 'abbbc']
###########

#2. + (plus) 1 oe more of the preseding charcter
print(re.findall(r"ab+c","ac abc abbc abbbc"))
#ot ['abc', 'abbc', 'abbbc']
###########

#3. ?(question) 0or 1 of the preseding character
print(re.findall(r"ab?c","ac abc abbc abbbc"))
#ot ['ac', 'abc']

##########
#4.{}(curely braces) exact or range of repetitions
print(re.findall(r"ab{3}c","ac abc abbc abbbc"))
#ot  ['abbbc']

################

#5. [](squRE braces) either b or c character set
print(re.findall(r"a[ae]d","abd acd aad aed"))
#ot ['aad', 'aed']

#6.[^] negated set not in set
print(re.findall(r"a[^ae]d","abd acd aad aed"))
#ot ['abd', 'acd']
########

#7() pareantheses grouping
print(re.findall(r"(ab)+","abd abab ab ababab"))
#ot ['ab', 'ab', 'ab', 'ab']
###############
#8 | (pipe) logical OR
print(re.findall(r"cat|dog", "I have a cat and a dog"))
#ot ['cat', 'dog']
###################
#9. re.sub() substitude using regex 
text = "My number is 123-456-7890"
print(re.sub(r"\d{3}-\d{3}-\d{4}", "***-***-****", text))
#ot My number is ***-***-****

#############
#10. re.split - split by pattern
print(re.split(r"[,;]", "apple,babana; grape,orange"))
#ot ['apple', 'babana', ' grape', 'orange']

##############
