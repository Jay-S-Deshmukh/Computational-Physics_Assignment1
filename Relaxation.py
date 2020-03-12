# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 15:51:31 2020

@author: Jay
"""
import numpy as np

A = [[0.2,0.1,1.,1.,0],[0.1,4.,-1.,1.,-1.],[1.,-1.,60.,0,-2.],[1.,1.,0,8.,4.],[0,-1.,-2.,4.,700]]
b = [1,2,3,4,5]
x_true = [7.859713071, 0.422926408, -0.073592239, -0.540643016, 0.010626163]

tolerance = 0.01
w=1.25

n = np.size(b)
x = np.zeros(n)

for i in range(50):
    for j in range(n):
        r = b - np.dot(A,x)
        x[j] = x[j] + w*r[j]/A[j][j]
    d = np.abs(x_true-x)
    if(all(p<tolerance for p in d )):
        break
        
print(x)
print(i)