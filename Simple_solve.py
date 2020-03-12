# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 19:16:52 2020

@author: Jay
"""

import numpy as np

A = np.array([[1,0.67,0.33],[0.45,1.,0.55],[0.67,0.33,1.]])
b = np.array([2,2,2])

print(np.linalg.solve(A,b))