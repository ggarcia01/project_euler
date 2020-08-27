'''
garcia, gil
created: 8/27/2020
last updated: 8/27/2020

project euler problem #7 description:

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.
What is the 10 001st prime number?
'''


#we have created a prime checker fxn before, so importing it to not repeat code
from PE_problem3 import isPrime

#we want to find the 10,001th prime number
ith_prime = 10001
#we will create a dictionary containing all prime numbers up to our target
prime_dict = {}
#the prime checker will check our i counter
i = 1
#we will use our j counter as the index to our dict
j = 1
while len(prime_dict) < ith_prime:
    if isPrime(i) == True:
        prime_dict[j] = i
        j+=1
    i += 1



print(prime_dict[10001])
