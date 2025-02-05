import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
x = [1, 7, 21, 35, 35, 21,  7, 1]
a1 = np.cos(x)
a2 = np.sin(x)
a3 = np.tan(x)
plt.plot(x,a1,'r')
plt.plot(x,a2,'c',marker='d',markersize=5,markeredgecolor='y')
plt.plot(x,a3,'k',linestyle='dashed')
plt.xlabel('ranu mandal')
plt.ylabel('pataka')
plt.show()

fib=[0,1,1,2,3,5,8,13,21,34]
sq=np.sqrt(fib)
plt.figure(figsize=(10,7))
plt.plot(range(1,11),fib,'co',markersize=5,linestyle='solid',markeredgecolor='r')
plt.plot(range(1,11),sq,'k+',markersize=7,linestyle='solid',markeredgecolor='r')
plt.xlabel('hi')
plt.ylabel('hello')
plt.show()
import os
current_working_directory = os.getcwd()

# print output to the console
print('it is:',current_working_directory)







