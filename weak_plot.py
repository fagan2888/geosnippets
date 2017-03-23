#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 21:19:48 2016

@author: huang
"""

import numpy as np
import matplotlib.pyplot as plt

proc = np.array([4,16,64])
runtime = np.array([63, 73, 68], dtype=float) #Seconds
#mem = np.array([89, 157, 435.5, 2060], dtype=float) #MB
weak_scale = runtime[0]/runtime

fig = plt.figure()               
plt.plot(proc, weak_scale, linewidth=2, marker='o')
plt.plot(proc, np.ones(len(proc)), linewidth=2)
plt.semilogx(basex = 2)
plt.title('Weak Scalability of the Navier-Stokes module')
plt.xlabel('Number of processors [-]')
plt.ylabel('Strong scalability [-]')
plt.legend(['RWTH cluster', 'Ideal cluster'], loc=4)
plt.ylim(0,1.1) 
plt.grid()
plt.savefig('weak_scalability.png')