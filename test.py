# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 16:06:25 2026

@author: shrih
"""

#Q1.Write a Python decorator called greet_decorator that adds the line "Hello!" before calling 
#any function. Use it on a function say_name() that prints "My name is Python.". 

def test_function():
    def say_name():
        return "My name is Python"
    return say_name 
Hello=test_function()
Hello()

#Q.2 Create an iterator that returns the squares of numbers from 1 to 5 using a custom class. 
def square_iterator():
    for i in range(1, 6):
        yield i * i

for value in square_iterator():
    print(value)

#Q.3Write a code example showing the difference between shallow copy and deep copy using a 
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
print("list",id(list_a))
print("list",id(list_b))

#Q.4 Create a class Car with attributes brand and model, and a method display() that prints the 
#brand and model of the car. Create an object and call the method.
car={"Model": "Nexon",
     "Brand":"TaTA",
     "since":"2023"}
car.items()

#Q.5 Write a function compress_string(s) that compresses repeated characters in a string using 
#the count of repetitions. For example:  
#compress_string("aaabbccdaa") → "a3b2c2d1a2"

def compress_stings():
    count =1
    
#[Q6] Load the following data into a Pandas DataFrame. Replace all marks less than 40 with the 
#value "Fail". 
import pandas as pd 
data = {'Name': ['Amit', 'Priya', 'John'],
        'Maths': [34, 67, 23], 
        'Science': [78, 29, 45]}      
df=pd.DataFrame(data)
df[['Maths','Science']] = df[['Maths','Science']].applymap(
    lambda x: "Fail" if x < 40 else x
)

print(df)

#Q7] Using NumPy, create two 1D arrays of size 5 with random integers from 1 to 20. Compute 
#the element-wise maximum and minimum between the two arrays.

import numpy as np

arr1 = np.random.randint(1, 21, 5)
arr2 = np.random.randint(1, 21, 5)

elementwise_max = np.maximum(arr1, arr2)
elementwise_min = np.minimum(arr1, arr2)

print("Array 1:", arr1)
print("Array 2:", arr2)
print("Element-wise Maximum:", elementwise_max)
print("Element-wise Minimum:", elementwise_min)

#[Q8] Using Seaborn, plot a boxplot for the following DataFrame to show the distribution of 
#marks across subjects:  
import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
import numpy as np
from scipy.stats import gaussian_kde  
data = pd.DataFrame({  
'Subject': ['Maths', 'Science', 'English', 'Maths', 'Science', 'English'],  
'Marks': [76, 89, 67, 45, 55, 91]  
}) 
df=pd.DataFrame(data)
df

plt.boxplot(data['Marks'])
plt.title('boxplot - subject_marks')
plt.show()
#Q.9  attempt all questions on numpy 
#a.  Create a 1D NumPy array with elements: 10, 20, 30, 40, 50. 
#b. Create a 2D array of shape (2,3). 
#c. Create: 
#An array of zeros (3x3) 
#An array of ones (2x4) 
#d. Generate numbers from 0 to 20 using arange(). 
#e.  Generate 10 evenly spaced numbers between 0 and 1 using linspace(). 
# Create a 3x3 identity matrix.

import numpy as np

arr=np.array([10,20,30,40,50])
print(arr)
 #   
import numpy as np
arr1=np.array([[10,20,30,],[60,70,90,]])
print(arr1.shape)
#
zero_matrix=np.zeros((3,3))
print("\n6.zero matrix:\n",zero_matrix)
#
ones_matrix=np.ones((2,4))
print("\n6.ones matrix:\n",ones_matrix)

#
import numpy as np

arr=np.arange(0,20)
arr
#
import numpy as np
arr=np.linspace(0,1,10)
arr
##
identity_matrix=np.eye(3,3)
print("\n.identity matrix:\n,",identity_matrix)
##
import seaborn as sns
import matplotlib.pyplot as plt

data_plot = pd.DataFrame({
    'Subject': ['Maths', 'Science', 'English',
                'Maths', 'Science', 'English'],
    'Marks': [76, 89, 67, 45, 55, 91]
})

sns.boxplot(x='Subject', y='Marks', data=data_plot)
plt.title("Distribution of Marks Across Subjects")
plt.show()
