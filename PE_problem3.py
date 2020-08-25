'''
garcia, gil
created: 8/24/2020
last updated: 8/24/2020

project euler problem #3 description:

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''


import numpy as np

TEST_VALUE = 600851475143


def isPrime(value):
    if value == 1:
        return False
    elif value == 2:
        return True
    else:
        for i in range(2,value):
            if value%i == 0:
                return False
        return True


def biggestPrimeFactor(value):
    lst = []
    for i in range(1, int(round(np.sqrt(value)))+1  ):
        if value % i == 0:
            lst += [i]
            lst += [value/i]
    prime_lst = []
    for j in lst:
        if isPrime(  int(j)  ) == True:
            prime_lst += [j]
    return np.max(prime_lst)




print(biggestPrimeFactor(TEST_VALUE))
