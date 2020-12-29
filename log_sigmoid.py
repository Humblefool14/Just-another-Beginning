import numpy as np
import math 
x = np.arange(0,8,0.001)
y = 1/(1+np.exp(-x))

z = (log2(2*x+0.486))/8 + 0.63
error = y-z
print(error)