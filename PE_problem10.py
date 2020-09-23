'''
garcia, gil
created: 8/29/2020
last updated: 9/23/2020

project euler problem #10 description:

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
import numpy as np
from datetime import datetime




#Sieve of Erastosthenes is an algorithm that finds primes up to N by
#finding all composites up to N, leaving only the primes
def SieveOfEratosthenes(n):
    #create a bool array of all True values representing each integer
    #from 0 to N.
    #we will change the bool value to False for each number that is composite
    bool_lst = [True for i in range(n+1)]
    bool_arr = np.array(bool_lst)
    #now we iterate from 2 to N to find all composite and convert their bool
    # value to False


    #for each num from 2 to N,
    for num in range(2,n+1):
        #if its corresponding bool value is true, then it is a prime
        if bool_arr[num] == True:
            #but any multiple of the prime is not prime
            i = 2*num
            while i <= n:
                #so change the corresponding bool value of these nums to false
                bool_arr[i] = False
                i = i + num

    #create a list of all nums up to N
    num_lst = list(range(n+1))
    #change it to arr
    num_arr = np.array(num_lst,dtype='int64')
    #index the num arr to only contain prime numbers, starting from 2
    return num_arr[bool_arr][2:]


startTime = datetime.now()

np.seterr(all='warn')

N = 2_000_000

primes = SieveOfEratosthenes(N)

print('sum of first {0} primes is:'.format(N), primes.sum())

print()
print('time')
print('------------------------')
print(datetime.now() - startTime)
