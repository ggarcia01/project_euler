'''
garcia, gil
created: 9/29/2020
last edited:9/29/2020

project euler prob # 12

The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.
What is the value of the first triangle number to have over five hundred divisors?
'''

import numpy as np


#first we create a function that returns a lst of all the factos of the inputted value
def factors(value):
    lst = []
    #to optimize, we only need to check up to sqrt(value gien) since the that will be its biggest factors
    for i in range(1, int(round(np.sqrt(value)))+1  ):
        if value % i == 0: #if any of the values between these two numbers divide it
            lst += [i] #add both factors to the list
            lst += [value/i]
    return lst #return the largest prime in the prime list


#intialize a list that will hold the factor for each number we test
t_num_lst = []
#intialize the triangle number, which will be updated each iteration
value = 0
for i in range(1,1_000_000): #the  range max just needs to be big enough to contain our desired number
    value += i #creates the next triangle number
    t_num_lst = factors(value) # finds the factors of the current triangle number
    #print('the n={} triangle num is {} and has {} factors'.format(i,value,len(t_num_lst)))
    if len(t_num_lst) > 500: #if there are more than 500 factors, break the loop
        break


print('{} is the first triangle number to have >500 factors. it is the {}th triangle num'.format(value,i))