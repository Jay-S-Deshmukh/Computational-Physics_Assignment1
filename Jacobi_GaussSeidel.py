# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 00:29:26 2020

@author: Jay
"""
import numpy as np

global x_true,tolerance

def iterate(T,c):
    x = np.zeros(np.size(b))
    for i in range(100):
        x = np.dot(T,x) + c
        d = np.abs(x_true-x)
        if(all(p<tolerance for p in d )):
            break
    return x,i

def jacobi(L,U,D):
    
    D_inv = np.linalg.inv(D)
    T = np.dot(D_inv,L+U)
    c = np.dot(D_inv,b)

    x,i = iterate(T,c)
    return x,i
    
def gauss_seidel(L,U,D):

    D_inv = np.linalg.inv(D-L)
    T = np.dot(D_inv,U)
    c = np.dot(D_inv,b)
    
    x,i = iterate(T,c)
    return x,i   

A = [[0.2,0.1,1.,1.,0],[0.1,4.,-1.,1.,-1.],[1.,-1.,60.,0,-2.],[1.,1.,0,8.,4.],[0,-1.,-2.,4.,700]]
b = [1,2,3,4,5]
x_true = [7.859713071, 0.422926408, -0.073592239, -0.540643016, 0.010626163]

tolerance = 0.01

U = np.triu(A)
L = np.tril(A)
D = L + U - A

L = D - L
U = D - U

x,i = jacobi(L,U,D)
dx = np.abs(x_true-x)

y,j = gauss_seidel(L,U,D)  
dy = np.abs(x_true-y)

print(x,dx,i)
print("*******")
print(y,dy,j)
  