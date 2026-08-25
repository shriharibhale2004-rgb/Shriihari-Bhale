x="""this is python.it is very powerful"""
print(x.upper())
#
print(x.lower())
#
x = " this is python "
x
print(x.strip())
#
x = " this is python "
x
print(x.lstrip())
#
x = " this is python "
x
print(x.rstrip())
#
x= "hello world"
print(x.replace("hello","gello"))
##############
x= "hello_world"
print(x.split("_"))
#
x= "hello world"
print(x.split(" "))
####
x="red-green-blue"
print(x.split("-"))
##
x='''this is python.It isvery simple to understand . difficult to implement'''
print(x.split("."))
##
input_colors = "red-blue-green-yellow"
def sorted_colors(input_colors):
    string_split=input_colors.split('-')
    string_split
    sort=sorted(string_split)
    sorted_string='-'.join(sort)
    return sorted_string
string_alphabetic=sorted_colors(input_colors)
print(string_alphabetic)
###
x='Hello world'
string1=x[::-1]
print(string1)
###
def is_palindrome(input):
    if input=="":
        return "You entered wrong input"
    else:
        string=input[::-1]
        if string==input:
            return True
        return False
    
print(is_palindrome("step on no pets "))
######
x="This is python and it is very powerful"
print(x.find("and"))

address='4/116 sunder apartment,suyognagar'
print(address.find('sundar'))
address[6:22]
######
#string concateness
x="Hello"
y="world"
print(x+y)
####
#to add white space
print(x+" "+y) 
#####
#string format
x=36
y="my name is Anthony"
print(x+y)

print(f"my name is anthony and my age is {x}")
#####
quantity=3
item_no=54
price=67
print(f"I want {quantity} pieces and item number is {item_no},its price is {price}")
########
my_order="I want {} pieces and item number is {},its price is {}"
print(my_order.format(quantity,item_no,price))
#####
quantity=3
item_number=54
price=67
my_order="I want {0} pieces and its item number is {1},its price is{2}"
print(my_order.format(quantity,item_number,price))
#####
#the escape character allows you to double quote
text="This is fun fare and it has got big \"round rigo\""
text="This is fun fare and it has got \"round rigo\""
print(text)
#####
#python boolean
print(10>9)
print(10<9)
print(10==10)
######
a=20
b=10
if(a>b):
    print("The a is greater than b")
else:
    print("b is greater than a")
#####
a=20
b=0
print(a!=b)
#######
#operator precedence
print(3*3+3/3-3)
#######
a=20
b=10
#identity operator
print(a is b)
print(a is not b)
########
a=20
b=10
print(a+b)
print(a-b)
print(2-3+6/8*2)
###
#python list
#append()
lst=["cherry","banana","apple"]
lst.append("mango")
print(lst)
#####
#clear removes all element from list
lst=["cherry","banana","apple"]
lst.clear()
print(lst)
######
#copy()method
lst=["cherry","banana","apple"]
lst2=lst.copy()
print(lst2)
######
#count
lst=["cherry","cherry","banana","apple"]
lst.count("cherry")
####
#expand()add elements in list
lst1=[1,2,3]
lst2=[4,5,6]
lst1=lst1+lst2
print(lst1)

lst.extend(lst1)
print(lst1)
#####
#insert()
lst=["cherry","banana","apple"]
lst.insert(0,"mango")
lst.insert(1,"kiwi")
print(lst)
#####
#pop operation
lst=["cherry","banana","apple"]
lst.pop(2)
lst.pop(0)
print(lst)
##reverse operation
lst=["cherry","banana","apple"]
lst.reverse()
print(lst)
##sort operation
lst=["cherry","apple","banana","kiwi"]
lst.sort()
print(lst)
##sorted with length
lst=["cherry","apple","banana","kiwi"]
sorted_lst=sorted(lst,key=len)
print(sorted_lst)
##created a nested list
nested_list= [1,2,3,],['a','b','c'],["true","false"]
print(nested_list)
# accessing thr element in nested list
nested_list[0][2]
nested_list[2][1]
#
nested_list[0]
#accessing thlast element of the lat element
nested_list[-1][-1]
nested_list[-3][-2]
#changing list 
nested_list[1][1]="F"
nested_list
##
our_faimily={
    "child":{
        "name":"ram",
        "dob":"21-05-2026"
        }
    }
# all element clear method
car = {
       "brand": "ford",
       "model": "mustang",
       "year":1964
       }
car.clear()
car
#copy method
car = {
       "brand": "ford",
       "model": "mustang",
       "year":1964
       }
x=car.copy()
print(x)

#fromkeys
#create a dictionary all keys
x={"key1","key2","key3"}
y=0
thisdict=dict.fromkeys(x,y)
thisdict
#get() get value
car = {
       "brand": "TaTa",
       "model": "siara",
       "year": 2026
       }
car.get("model")
#d
car = {
       "brand": "TaTa",
       "model": "siara",
       "year": 2026
       }
car.items()
#display of all values
car = {
       "brand": "ford",
       "model": "mustang",
       "year": 1964
       }
car.values()
#insert item 
car = {
       "brand": "ford",
       "model": "mustang",
       "year": 1964
       }
car.update({"color":"white"})
car
#
car = {
       "brand": "ford",
       "model": "mustang",
       "year": 1964
       }
car.update({"brand":"maruti"})
car
## sort by key
data = {'b':2,'a':3,'c':1}
data.items()
sorted_by_keys = dict(sorted(data.items()))
print(sorted_by_keys)
##sort by values
data = {'b':2,'a':5,'c':1}
sorted_by_values = dict(sorted(data.items(), key=lambda item: item[1]))
print(sorted_by_values)
##
sorted_dict = {"banana":40,"apple":100,"grapes":120,"mango":200}
free_item_key = min(sorted_dict, key=sorted_dict.get)
free_item_value = sorted_dict[free_item_key]
print(f"You will get the lowest priced item '{free_item_key}' ({free_item_value}) for free.")
###
sorted_dict = {"banana":40,"apple":100,"grapes":120,"mango":200}
free_item_key =max(sorted_dict, key=sorted_dict.get)
free_item_value = sorted_dict[free_item_key]
print(f"you will get the  highest priced item {free_item_key} ({free_item_value}) for free.")
##
# sorted by desending order
sorted_by_value_desc = dict(sorted(sorted_dict.items(),key=lambda item: item[1],reverse=True))
print(sorted_by_value_desc)
###

dict1 = {'apple':'100','grapes':'120','mango':'200','banana':'40'}
total=0
for value in dict1.values():
    total=total+int(value)
print(total)    

## another way of calulating sum
dict1 = {'apple':'100','grapes':'120','mango':'200','banana':'40'}
#convert values to inte
total_sum = sum(int(value) for value in dict1.values())
print(total_sum)

#concatenet of dictionary
dict1={1:10,2:20}
dict2={3:30,4:40}
dict3={5:50,6:60}
dict1.update(dict2)
print(dict1)
dict1=dict1|dict3
print(dict1)
###
dict1={'a':20,'b':30}
print('a' in dict1)

### function without argument
def my_function():
    print("hello from a function")
    
my_function()
##function with an argument
def my_function(name):
    print("hello "+ name)
    
my_function("ram")
##
#function with positional argument

def my_function(name1,name2):
    print(name1+" "+name2)
    print(name1+" "+name2)
my_function("hello","world")  
my_function("world","hello")  
##
#arbitary argument *args
def my_function(*args):
    print(args[0]+" "+args[2])
    
my_function("Tappu","Sonu","Goli")
##
#function with kwargs
def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} : {value}')
my_function(first_name="popalal", mid_name="mohanlal",last_name="goyal")
## function with default value

def my_function(country ="Norway"):
    print("I am from "+country)
my_function("Dubai")
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")   
##passing a list an a argument

fruits=["orange","banana","guava"]
def my_function(fruits):
    for x in fruits:
        print(x)
my_function(fruits)        
    
# function with return value 
def my_function(x):
    y=x*5
    return y
my_function(5)

def my_function(x):
    y=x*5
    z=x*7
    return y,z
my_function(5)
## pass passing function
def my_function():
    pass
my_function()

# recursive function 
def factorial(x):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))
factorial(1)
factorial(6)    
##
def add(a):
    sum=a+10
    return sum
add (20)    


add=(lambda a:a+10)
print(add(20))
#multiple function can take any no 
add=lambda a,b:a+b
print(add(5,6))
###
text = "Python123"
print(text.isalpha())
print(text.isdigit())
print(text.isalnum())
#3

text1 = "HELLO"
text2 = "Hello123"
text3 = "12345"
count1=0
for i in range(len(text1)):
    if text1[i].isupper():
        count1=count1+1

print(count1)   



text1 = "HELLO"
text2 = "Hello123"
text3 = "12345"
count2=0
for i in range(len(text1)):
    if text2[i].islower():
        count2=count2+1

print(count2) 

text1 = "HELLO"
text2 = "Hello123"
text3 = "12345"
count3=0
for i in range(len(text1)):
    if text3[i].islower():
        count3=count3+1

print(count3)      
###

def plus_one(number):
    number1= number + 1     
    return number1
plus_one(5)


##defining function inside other function
def plus_one(number):
    def add_one(number):
        number1=number+1
        return number1
    result = add_one(number)
    return result
plus_one(5)

#passing function an argument

def plus_one(number):
    result1= number +1 
    return result1
def function_call(function):
    result= function(5)
    return result
function_call(plus_one)

##
print("HEllo KIRAN")

def my_function(x):
        print(x)
        
my_function("kiran")
#####
our_family={
    "child":{
        'name':'sham',
        'dob':'20-19-2003'
        
        }
    }
print(our_family)
##
def add(a):
    sum=a+10
    return sum
add(20)
##
add=lambda a:a+10
print(add(20))
##
add=lambda a,b:a+b
print(add(5,6))
###

def left_rotate(lst, d):
    n=len(lst)
    d= d % n
    
    rot_text = lst[d:]+ lst[:d]
    return rot_text
lst=[1,2,3,4,5]
d=2 
lst[d:]
lst[:d]
##
mat = [
       [1,2,3],
       [4,5,6],
       [7,8,9]
       ]
rows = len(mat)
cols = len(mat[0])

for i in range(rows):
    for j in range(cols):
        print(f"element in [{i}][{j}] are {mat[i][j]}")
              
###
#addition of two matrices
mat1=[[1,2,3],
      [4,5,6],
      [7,8,9]]
mat2=[[1,2,3],
      [4,5,6],
      [7,8,9]]
result=[[0,0,0],
        [0,0,0],
        [0,0,0]
        ]      
rows=len(mat1)
cols=len(mat1[0])
for i in range(rows):
    for j in range(cols):
        result[i][j]=mat1[i][j]+mat1[i][j]
result        
##
#find digonal element of matrix
fmat1=[[1,2,3],
      [4,5,6],
      [7,8,9]]
rows=len(mat1)
cols=len(mat1[0])
for i in range(rows):
    for j in range(cols):
        if i==j:
            print(mat1[i][j])
## check thr given matrix is sparse or not    
mat1=[[1,0,0],
      [0,0,2],
      [0,1,1]]
rows=len(mat1)
cols=len(mat1[0])
count=0
for i in range(rows):
    for j in range(cols):
        if mat1[i][j]==0:
            count+=1 
if count>(rows*cols)/2:
    print('Sparse')
else:
    print('not sparse')
##
def is_leap(year):
    if (year%4==0 and year%100!=0) or (year%400==0):
        print(f"{year} is leap year") 
    else:    
        print(f"{year} is not leap year") 
is_leap(1900)        
##
score=int(input("Enter the score"))
if (score<400 or score>850):
    print("Invalid")
else:
    if 400<=score<600:
        print('s')
    elif 600<=score<800:
        print('m')
    else:
        print('p')
## write a function to reaverse the number
num=int(input("enter the number"))
while(num!=0):
     digit=num%10
     print(digit,end='')
     num=num//10  
###
num=input("enter the number")
for digit in num[::-1]:
    print(digit,end=' ')
##write program to calculate sum of odd or even no in list

num=[1,3,5,8,10]
total=0
for i in range (len(num)):
    if num[i]%2==0 or num[i]%2!=0:
        total=total+num[i]
print(total)    
##
num=[2,4,6,8,10]
total=0
for i in range(len(num)):
    if num[i]%2==0: 
        total=total+num[i]
print(total)        
#
num=[1,3,7,9]
total=0
for i in range(len(num)):
    if num[i]%2!=0:
        total=total+num[i]
print(total)     

#
total=sum(i for i in num if i%2==0 or i%2!=0)
print(total)    

##write program to calculate sum of digit in number
num=int(input("enter the number"))
total=0
while(num!=0):
    digit=num%10
    total=total+digit
    num=num//10
print(total)    
##calculate sum of digit 
#which are multiple of 3
num=int(input("enter the number"))
total=0
while(num!=0):
    digit=num%10
    if digit in(3,6,9):
        total=total+digit
    num=num//10
print(total)        
#
num=int(input("enter the number"))
total=0
while(num!=0):
    digit=num%10
    if digit in(2,3,5,7):
        total=total+digit
    num=num//10
print(total)    
###
#count the number of digit in a number
num=int(input("enter the number"))
count=0
while(num!=0):
     digit=num%10
     count=count+1 
     num=num//10
print(count)     
###how many times no in count
num=int(input("enter the number"))
digit=int(input("witch digit is to count"))
count=0
while(num!=0):
    if num%10==digit:
        count=count+1 
    num=num//10
print(count) 
### program for check duck no or not
num=int(input("enter the number"))
is_duck=False
while(num!=0):
    digit=num%10
    if digit==0:
        is_duck=True
    num=num//10
if is_duck:
   print('the number is duck')
else:
   print('the number is not duck')    
##find reverse number
num=int(input("enter the number"))
reverse_num=0
while(num!=0):
    digit=num%10
    reverse_num=reverse_num*10+digit
    num=num//10
print(reverse_num)    
### 
num=int(input("enter the number"))
lst=[]
while(num!=0):
    digit=num%10
    lst.append(digit)
    num=num//10
print(*lst) #unfolding of list    
##
num=input('enter the number')[::-1]
print(num)    
##faboneis series
num=int(input("Enter the number"))
n1,n2=0,1 
print(n1,n2,end=' ')
for i in range(2,num):
    n3=n1+n2
    print(n3,end=' ')
    n1,n2=n2,n3
##
num=int(input("enter the number"))
def fib(n):
    if n==0 or n==1: 
         return n 
    else:
        return fib(n-1)+(n-2)
    
for i in range (0,num):
     print(fib(i),end=' ')    
##niven number
num=int(input("enter the number"))
result=0
temp=num
while(num!=0):
    digit=num%10
    result=result+digit
    num=num//10
if num%result==0:
   print("number is niven")
else:
   print("number is not niven")    
##spcial number
num=int(input("enter the number"))
digit1=num%10
digit2=num//10
if num==((digit1+digit2)+(digit1*digit2)):
    print("number is special")
else:
    print("nuber is not special")  
#prime number
def prime_num(num):
    if num < 2:
        return "the number is not prime number"
    for i in range(2,int(num**0.5)+1):
        if num%1 ==0:
            return "the number is not prime "
    return "the number is prime"
print(prime_num(2))   
print(prime_num(3)) 
print(prime_num(5))
print
## bouble sort 
n= int(input())
arr = list(map(int, input().split()))
for i in range (n - 1):
    for j in range(n - 1 - i):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(*arr)            
## find duplicates from given list
lst = [4,5,2,4,3,2,1,5,6]
uniqe_lst = list(set(lst))
uniqe_lst

print("original array:",lst)
print("array after eliminating duplicates:",uniqe_lst)
####mario pyramid diplay 
#for a square 
for i in range(5):
    for j in range(2):
        print("$",end=' ')
    print()    
# for a pyramid
for i in range(4):
    for j in range(i+2):
         print("#",end=' ')
    print()     

for i in range(4):
    for j in range(4-i):
         print("#",end=' ')
    print() 
    
for i in range(4):
    for j in range(5-i):
         print("#",end=' ')
    print()     
    
#dispaly symetric triangle
 
rows=4
for i in range(rows):
    for j in range(rows - i - 1):
        print(" ",end=" ")
        
    for k in range(i + 1):
        print("#", end="   ")
        
    print()
    
##odd or even array 
n = int(input())
arr = list(map(int,input().split()))
odd = []
even = []
for num in arr:
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)
result = even + odd
print(result)
 

##
#
time_input = input()

#   
hh, mm=map(int, time_input.split(':'))
#
minutes_passed=0 
#
while True:
    hh_str =str(hh).zfill(2)
#step6:convert minute to 2digit string    
    mm_str =str(hh).zfill(2)
#step7:combine hour and minute    
    time_str = hh_str + mm_str 

#step8:check if the time is palindrome
    if time_str == hh_str[::-1]:
        #if time reads same forward and backword
        print(f"user will get power after {minutes_passed} minute")
        #clear ,meaningful output
        break
    #exit loop once answer is found
#step9:move forward by 1minute
    mm +=1 
    minutes_passed+=1 
# step10:hamdle minute overflow
    if mm==60:
        mm=0 
        hh+=1 
#step 11: handle hour overflow (24hours clock)
    if hh==24:
       hh=0  
#################

input1 = "Wipro Technologies"

words = input1.split()
words
char_lists = [list(word) for word in words]
char_lists
letter_counts= [len(chars) for chars in char_lists]
letter_counts
print("Character lists:",char_lists)
print("letter counts:",letter_counts)
def sum_digits(num):
    total=0
    while num!=0:
       last_digit=num%10 
       total=total+last_digit
       num=num//10 
    return total
total=[sum_digits(i)for i in letter_counts] 
total
total_sum=0 
for i in total:
    total_sum=total_sum+i
total_sum
if(total_sum//10)!=0:
   total=sum_digits(total_sum)
   print(total)
else:
   print(total_sum)            
##
input1= "data science and ai"
##
input1="Bigdata analytics machine learning"
##
input1="python"
##
input1=""
##
input1="  "
##
input1="AI 101 @Home"
#
input1 = ""

words = input1.split()
words
char_lists = [list(word) for word in words]
char_lists
letter_counts= [len(chars) for chars in char_lists]
letter_counts
print("Character lists:",char_lists)
print("letter counts:",letter_counts)
def sum_digits(num):
    total=0
    while num!=0:
       last_digit=num%10 
       total=total+last_digit
       num=num//10 
    return total
total=[sum_digits(i)for i in letter_counts] 
total
total_sum=0 
for i in total:
    total_sum=total_sum+i
total_sum
if(total_sum//10)!=0:
   total=sum_digits(total_sum)
   print(total)
else:
   print(total_sum)            
