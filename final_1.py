import numpy as np 
import math 
 
x = np.arange(0,8,0.001)
x= x*pow(2,5)
print(x)
x = np.round_(x)

log_constant = math.log(math.exp(1),2)
log_constant = log_constant*pow(2,7)
log_constant = round(log_constant)


print(log_constant)
print(type(log_constant))

x = x*(log_constant)
mul_add = 1 << 8
print(mul_add)
x = x + mul_add
x = x/pow(2,8)


print(x)
print(type(x))

y = np.log2(x)
y = np.ceil(y)
print(y)

frac_x = pow(2,y)-x
print(frac_x)
