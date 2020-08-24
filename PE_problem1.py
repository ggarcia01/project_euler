'''
garcia, gil
created: 8/24/2020
last updated: 8/24/2020

project euler problem #1 description:

if we list all the natural numbers below 10 that are multiples of 3 or 5, we get
3,5,6, and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

sum = 0 #initialize the sum variable which we will add all multiples of 3 or 5 to
for i in range(1000): # for all values below 1,000
    if i%3 == 0 or i%5 == 0: #if the value is divisible by 3 or 5 w.o having a remaninder, then it is divisible
        sum += i #so add it to our sum value


print('the sum of all multiples of 3 or 5 below 1,000 is: ',sum)
