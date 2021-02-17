# Hello Python

# HMW 1 : Generating a 3x3 matrix with 9 'prime' numbers using the for loop.

import random as rnd 
import secrets as scr

primeNumberList = []

for num in range(1,100):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           primeNumberList.append(num)

for i in range(3):
  print(scr.choice(primeNumberList), scr.choice(primeNumberList), scr.choice(primeNumberList))
