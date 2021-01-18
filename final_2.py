import numpy as np 
import math 
 
x = np.arange(0,8,0.001)
log_constant = math.log(math.exp(1),2)
print(log_constant) 

x = x*(log_constant)
print(x)

#x = x*pow(2,12)
#x = x + (1 << 8)
#x = x/pow(2,8)print(x) 

y = np.ceil(x)
print(y)

frac_x =  y-x
print(frac_x)
