# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 16:29:47 2026

@author: shrih
"""
##arr in numpy
import numpy as np
arr=np.array([10,30,20])
print(arr)
##
#multidimentional array
#create multidimentional arr
arr=np.array([[10,20,30],[40,50,60]])
print(arr)
##
#represent 
arr=np.array([10,20,30,40],ndmin=3)
print(arr)
###
arr=np.array([10,20,30],dtype=complex)
print(arr)
###
arr=np.array([[1,2,3,4],[7,8,9,6],[5,8,9,7]])
print(arr.ndin)
print(arr)
#find each item in array
arr=np.array([10,20,30,])
print('EAch item contain in bytes:',arr.itemsize)
##shape and size
arr=np.array([[10,20,30,40],[60,70,80,90]])
print("array size:",arr.size)
print("array shape:",arr.shape)
##create array from list with type float
arr=np.array([[10,20,30],[40,50,60]],dtype='float')
print("array create by using :\n",arr)
##create sequence of int using arange()
arr=np.arange(0,20,3)
print("A sequential array eith steps of 3:\n",arr)
##array indexing in numpy

arr=np.arange(11)
print(arr)
#
print(arr[2])
#
print(arr[-2])
##multidimentional array indexing 
#access multi dimentional array element
#using array indexing
arr=np.array([[10,20,30,40,50],[20,30,50,10,30]])
print(arr)
#
print(arr.shape)
#
print(arr[1,1])
#print
print(arr[0,4])
#
print(arr[1,-1])
#
print(arr[0,0])
#
print(arr[1,-2])
print(arr[0,-2])
##
#access array element using slicing
arr=np.array([0,1,2,3,4,5,6,7,8,9])
x=arr[1:8:2]
print(x)
#
x=arr[-2:3:-1]#start last but one(-2)upto3 but not 3 in step of
print(x)
#
x=arr[-2:10]
print(x)
#
import numpy as np
#indexing in numpy
multi_arr=np.array([[[10,20,10,30],
                     [40,50,70,80],
                     [60,10,70,90],
                     [30,90,40,30]]])
multi_arr

print(multi_arr[0, 0])
multi_arr[1,3]
multi_arr[1,:]
multi_arr[:,1]

#
import numpy as np
arr=np.arange(35).reshape(5, 7)
print(arr)
##boolean array indexing
import numpy as np
arr=np.arange(12).reshape(3,4)
print(arr)

rows=np.array([False,True,True])#not 0th row only first and 
rows
wanted_rows=arr[rows,:]
print(wanted_rows)
#create array
array=np.array([10,20,30,40])
print("Array:",array)
print(type(array))
#convert list
lst=array.tolist()
print('list:',lst)
print(type(lst))
#convert multi dimentional array to list
array=np.array([[10,20,30,40],
                [50,60,70,80],
                [60,40,30,10]])
print("array:",array)

lst=array.tolist()
print("list:",lst)


#use asarray
list=[20,40,60,80]
array=np.asarray(list)
print('array',array)
print(type(array))
##
array=np.array([[[1,2,3],[4,5,6]]])
array
print(array.shape)
print(array.ndim)
print(array.itemsize)
print(array.size)
print(array.dtype)
##
#resize the arr
array=np.array([[[10,20,40],[40,50,60]]])
array.shape=(3,2)
print(array)
###
#reshape usage
array=np.array([[10,20,30],[40,50,60]])
new_array=array.reshape(3,2)
print(new_array)
####################
import numpy as np
#1 square matrix(same number of rows and column)
square_matrix=np.array([[1,2],[3,4]])
print("1. Square Matrix:\n",square_matrix)
#2 rectangle matrix(rows and column)
rect_matrix=np.array([[1,2,3],[4,5,6]])
print("\n2.rectangle matrix:\n",rect_matrix)
#3
diagonal_matrix=np.diag([10,20,30])
print("\n3.Diagonal matrix:\n",diagonal_matrix)
##
scalar_matrix=np.diag([5,5,5])
print("\n4.scalar matrix:\n",scalar_matrix)
###
identity_matrix=np.eye(3)
print("\n.identity matrix:\n,",identity_matrix)
###
zero_matrix=np.zeros((3,3))
print("\n6.zero matrix:\n",zero_matrix)
###
ones_matrix=np.ones((3,3))
print("\n7.ones matrix",ones_matrix)
####
upper_triangle=np.array([[1,2,3],
                         [0,4,5],
                         [0,0,6]])
print("\n8.upper matrix;\n",upper_triangle)
###########
lower_trangular=np.array([[1,0,0],
                          [2,3,0],
                          [4,5,6]])
print("\n9. lower matrix ;\n",lower_trangular)
###
symentric_mtrix=np.array([[1,7,3],
                          [7,4,-5],
                          [3,-5,6]])
print("\n10. symentric matrix ;\n",symentric_matrix)
#####
skew_symmentric=np.array([[0,2,-1],
                         [-2,0,-4],
                         [1,4,0]])
print("\n11. skew symmentric \n",skew_symmentric)
#
sparse_matrix=np.array([[0,8,0],
                        [0,0,0,],
                        [0,0,0]])
print("\n12.sparse matrix",sparse_matrix)
#########
row_matrix=np.array([[1,2,3]])
print('\n13 row matrix',row_matrix)

column_matrix=np.array([[1],
                        [2],
                        [3]])
print("\n .column matrix ", column_matrix)

#####
import numpy as np
A= np.array([[1,2],[3,4]])
B=np.array([[5,6],[7,8]])
addition=A+B
print("\nmatrix addition ;\n",addition)

subtraction=A-B
print("\nmatrix subtraction;\n",subtraction)

scalar_mult=2*A
print('\nmatrix multiplication ',scalar_mult)

matrix_mult=np.dot(A,B)
print("nmatrix mult dot product",matrix_mult)
##
transpose_A=A.T
print('\ntranspose of A:\n',transpose_A)
#
det_A=np.linalg.det(A)
print("\n det_A",det_A)

#
if np.linalg.det(A)!=0:
    inverse_A=np.
    
    
#############


A
trace_A=np.trace(A)
print("\n.trace of a\n",trace_A)    

##
eig_vals,eig_vecs=np.linalg.eig(A)
print("\neigenvalues of a",eig_vals)
print("\neigenvectors of a",eig_vecs)
