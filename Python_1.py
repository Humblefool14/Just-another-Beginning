import math
import matplotlib.pyplot as plt
x =2;
y = 1/(1+math.exp(-x))
print (y)
sum =0;
for i in range(0,10):
    sum = sum+pow(-1,i)*(math.exp(-i*x));
    print((sum-y))

fig = plt.figure();
