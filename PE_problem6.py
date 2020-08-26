'''
garcia, gil
created: 8/26/2020
last updated: 8/26/2020

project euler problem #5 description:

The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
    (1+2+ ... + 10)^2 = 55^2 = 3025
Hence the difference between
the sum of the squares of the first ten natural numbers and the square of the sum is:
        3025 - 385 = 2640.
Find the difference between
the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

# initializing variables which will be updated throughout the below for loop
sum_of_squares = 0
sum_of_100 = 0

for i in range(1,101): #for the first 100 values
    sum_of_squares += i**2 # sum the square of each value
    sum_of_100 += i #sum the value

square_of_sum = sum_of_100**2 #square the sum of the first 100 values

difference = square_of_sum - sum_of_squares #difference

print(square_of_sum, 'minus', sum_of_squares, 'equals', difference)
