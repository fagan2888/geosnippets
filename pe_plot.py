# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

proc = np.array([1.,2.,4.,8.,16.,32.])
runtime = np.array([2180.,1232.,641.,404.,250.,157.])
scale = runtime[0]/runtime
eff = scale/proc


plt.figure()
plt.plot(proc, scale, linewidth=2)
plt.plot(proc, proc, linewidth=2)
plt.loglog(basex = 2, basey = 2)
plt.title('Strong scalability of the Navier-Stokes module')
plt.xlabel('Number of processors [-]')
plt.ylabel('Strong scalability [-]')
plt.legend(['RWTH cluster', 'Ideal cluster'], loc=4)
plt.grid()
plt.savefig('scalability.png')

plt.figure()
plt.plot(proc, eff, linewidth=2)
plt.plot(proc, proc/proc, linewidth=2)
plt.semilogx(basex = 2)
plt.title('Parallel efficiency of the Navier-Stokes module')
plt.xlabel('Number of processors [-]')
plt.ylabel('Parallel efficiency [-]')
plt.legend(['RWTH cluster', 'Ideal cluster'], loc=4)
plt.ylim(0,1.1)
plt.grid()
plt.savefig('parallel_efficiency.png')