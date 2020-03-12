# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 18:51:54 2020

@author: Jay
"""
import numpy as np
import time
'''
def decompose_qr(A):
    
    n = np.size(A[0])
    Q = np.zeros((n,n))
    R = np.zeros((n,n))
   
    for i in range(n):
        Q[:,i] = A[:,i]
        for j in range(i):
            Q[:,i] = Q[:,i] - np.dot(Q[:,j],A[:,i])*Q[:,j]
        Q[:,i] = Q[:,i]/np.linalg.norm(Q[:,i])
        
    for i in range(n):
        for j in range(i+1):
            R[j][i] = np.dot(Q[:,j],A[:,i])
    return Q,R
'''
def eigen(C):
    W = np.eye(np.size(C[0]))
    for i in range(20):
        Q,R = np.linalg.qr(C)
        #Q,R = decompose_qr(C)
        C = np.dot(R,Q)
        W = np.dot(W,Q)
    return np.diag(C),W

M = np.array([[0,1,1],[0,1,0],[1,1,0],[0,1,0],[1,0,1]])

start_manual = time.time()

A = np.dot(np.transpose(M),M)
B = np.dot(M,np.transpose(M))

A_val,V = eigen(A)
idx = A_val.argsort()[::-1]   
A_val = A_val[idx]
V = V[:,idx]
#print(np.dot(V,np.dot(S,np.transpose(V))))

B_val,U = eigen(B)
idx = B_val.argsort()[::-1]   
B_val = B_val[idx]
U = U[:,idx]
#print(np.dot(U,np.dot(S_dummy,np.transpose(U))))

s = np.sqrt(A_val)
Ans = [U,s,np.transpose(V)]
end_manual = time.time()

'''
S = np.zeros(M.shape)
np.fill_diagonal(S,s)
print(np.dot(U,np.dot(S,np.transpose(V))))
'''

start_auto = time.time()
print(np.linalg.svd(M))
end_auto = time.time()

print("Manual implementation:",end_manual-start_manual)
print("Numpy function:",end_auto-start_auto)
#print(s,s_true)
#print(np.abs((s-s_true)/s_true)*100)
