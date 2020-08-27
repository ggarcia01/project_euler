'''
garcia, gil
created: 8/25/2020
last updated: 8/25/2020

project euler problem #5 description:

2520 is the smallest number that can be
divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?
'''



def method1(value):
    divisible_by = value


    bool = False
    value = divisible_by #start at 20 since nums < 20 arent divisible all nums 1-20
    while bool == False:
        bool_lst = [] #appending true/false depending on wheter the nums 1-20 divide it evenly
        for i in range(1,divisible_by + 1):
            if value%i ==0: #if any nums divide it evenly
                bool_lst += [True] #append true
            else:
                bool_lst += [False] #otherwise, append false
        if False not in bool_lst: #if all bool values = True, then we found our value
            bool = True
        else:
            value += divisible_by #otherwise, add 20 to value variable and search again





'''

another way to solve p5:


idea ->

make isPrime() fxn
make primeFactors() fxn


list =[]
for  i in 1-20:
    if isPrime(i) is true:
        add # to list
    if i is not prime:
        find prime factors using primeFactors()
        add primeFactors to list


prod = 1
for i in len(list):
    prod *= i

our answer is i

'''

from PE_problem3 import isPrime
import numpy as np



def primeFactors(value):
    lst = []
    #to optimize, we only need to check up to sqrt(value gien) since the that will be its biggest factors
    for i in range(1, int(round(np.sqrt(value)))+1  ):
        if value % i == 0: #if any of the values between these two numbers divide it
            lst += [i] #add both factors to the list
            lst += [value/i]
    prime_lst = []
    for j in lst: #for any value in the list, if it is prime, add it to the prime list
        if isPrime(  int(j)  ) == True:
            prime_lst += [j]
    return prime_lst #return the largest prime in the prime list



def method2(value):
    prime_factors = []
    for i in range(1,value+1):
        prime_factors += primeFactors(i)
        print(i,primeFactors(i))
    prod = 1
    print(prime_factors)
    for j in prime_factors:
        prod *= j
    return prod

print( method2(10))



'''
need to figure out way to not over count prime factors.

if factors in our prime list can already be multiplied to create the next number in list,
no extra factors need to be added.


ex: if we have collected factors for 1 - 3, then we have the list:
[1,2,3]
for 4, the prime factors are 2 and 2.
we only need to add one 2 since theres already a 2 in ourlist that can mulitply w the new 2 make 4.


'''
