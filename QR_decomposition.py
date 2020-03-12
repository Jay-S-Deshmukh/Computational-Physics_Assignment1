# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 16:06:55 2020

@author: Jay
"""

import numpy as np

A = [[5.0,-2.0],[-2.0,8.0]]

A_old = A
for i in range(12):
    Q,R = np.linalg.qr(A_old)
    A_new = np.dot(R,Q)
    A_old = A_new

print(A_old)
print(np.linalg.eigvals(A))