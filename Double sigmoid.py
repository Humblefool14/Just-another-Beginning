#paper : New paper (2019) 

import numpy as np
import math
def sigm(x):
    sum =0
    for i in range(0,6):
        sum = sum+pow(-1,i)*(math.exp(-i*x))
    return sum            
    
x =np.arange(0,8,0.001)
y = 1/(1+np.exp(-x))
sum =[0 for i in range(0,np.size(x))]
error = [0 for i in range(0,np.size(x))]

for j in range(0,np.size(x)):
    if(x[j]<=1):
        sum[j]= (sigm(x[j]+2)+1-sigm(abs(x[j]-2)))/2
    else :
        sum[j] = sigm(x[j])
    
#print(sum)    
error=sum-y
for i in range(0,np.size(x)):
    print(error[i])
# print(np.var(error))
# print(np.std(error))
# print(np.mean(error))
# print(max(abs(error)))

#Error : calculating two sigmoid terms increases error at certain points to 0.1
