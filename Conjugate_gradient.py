# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 17:11:10 2020

@author: Jay
"""

import numpy as np

A = [[0.2,0.1,1.,1.,0],[0.1,4.,-1.,1.,-1.],[1.,-1.,60.,0,-2.],[1.,1.,0,8.,4.],[0,-1.,-2.,4.,700]]
b = [1,2,3,4,5]
x_true = [7.859713071, 0.422926408, -0.073592239, -0.540643016, 0.010626163]

tolerance = 0.01

n = np.size(b)
x = np.zeros(n)

d = b - np.dot(A,x)
p=d
for i in range(20):
   if(all(p<tolerance for p in d )):
        break
   a = np.dot(d,d)/np.dot(p,np.dot(A,p))
   x = x + a*p
   d_new = d - a*np.dot(A,p)
   b = np.dot(d_new,d_new)/np.dot(d,d)
   p = d_new + b*p
   d = d_new
    
print("Solution:",x)
print("No. of iterations:",i)