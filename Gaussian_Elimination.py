# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 18:20:59 2020

@author: Jay
"""

import numpy as np

def pivot(A,b,k):
     
    j=k
    for i in range(k,np.size(b)):
        if(np.abs(A[j][k])<np.abs(A[i][k])):
            j=i
    
    A[[k,j]] = A[[j,k]]
    b[k],b[j] = b[j],b[k]
    
    return A,b

def gauss(A,b,k):
    
    if((np.size(b)-k)==1):
        try:
            b[k] = b[k]/A[k][k]
            A[k] = A[k]/A[k][k]
            return A,b
        except: return -1,-1
          
    else:
        A,b = pivot(A,b,k)
        try:
            b[k] = b[k]/A[k][k]
            A[k] = A[k]/A[k][k]
        
            for i in range(np.size(b)-k-1):
            
                if(A[k+i+1][k]==0): continue
                b[k+i+1] = b[k+i+1] - b[k]*A[k+i+1][k]
                A[k+i+1] = A[k+i+1] - A[k]*A[k+i+1][k]
             
            return gauss(A,b,k+1)
    
        except: return -1,-1
        

A = np.array([[1.0,0.0],[1.0,0.0]])
b = np.array([2.0,0.0])
n = np.size(b)

A,b = gauss(A,b,0)

print(A)
print(b)

if(isinstance(A,int)): print("A is a singular matrix!")

else:
    sol = np.zeros(n)
    
    for i in range(n-1,-1,-1):
        sol[i] = b[i]
        for j in range(i+1,n):
            sol[i] = sol[i] - A[i][j]*sol[j]
        
    print(sol)