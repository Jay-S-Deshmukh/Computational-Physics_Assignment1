# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 16:39:20 2020

@author: Jay

"""
import numpy as np

A = [[2.,-1.,0.],[-1.,2.,-1.],[0.,-1.,2.]]

b = [1,0,0]

b_eig = b

for i in range(9):
    
    b_eig = np.dot(A,b_eig)

b_final = np.dot(A,b_eig)
eig = np.dot(b_final,b)/np.dot(b_eig,b)

eig_true = np.linalg.eigvals(A)[0]

print(eig,eig_true)
print(np.abs((eig_true - eig)*100/eig_true))
