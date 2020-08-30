'''
garcia, gil
created: 8/29/2020
last updated: 8/29/2020

project euler problem #8 description:

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
What is the value of this product?
'''


import numpy as np

#defining a fxn that calculates all pyhagorean tripes up until a = 1,000
def pythragorean_triples(limit):
    for a in range(limit): #for every a up until the limit
        for b in range(1,a): #for every b up until a
            c = np.sqrt(a*a + b*b) #calculate the square root of a^2 + b^2
            if c%1 == 0: #if it is a whole number, it is a perfect square
                sum = a+b+c #find the sum of it
                if sum == 1000: #if it is equal to 1,000
                    return [a,b,c] #return the integers that make up the triplet



py_trip = pythragorean_triples(1000)
print(py_trip)


#find the product of the triplet
prod = 1
for element in py_trip:
    prod *= element

print(prod)
