'''
garcia, gil
created: 8/24/2020
last updated: 8/25/2020

project euler problem #3 description:

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''


import numpy as np

TEST_VALUE = 600851475143


def isPrime(value):

    #checking edge cases
    if value < 0 or value == 0 or value == 1:
        return False
    elif value == 2:
        return True
    else:
        #for every other number
        #test for divisibility between 2 and the given number
        for i in range(2,  int(round(np.sqrt(value))+1)):
            if value%i == 0: #if any divide w.o a remainder
                return False #the number is not a prime
        return True #otherwise, it is


def biggestPrimeFactor(value):
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
    return np.max(prime_lst) #return the largest prime in the prime list




print(biggestPrimeFactor(TEST_VALUE))
