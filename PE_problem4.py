'''
garcia, gil
created: 8/25/2020
last updated: 8/25/2020

project euler problem #4 description:

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

#we want to define a palindrome checker to use later
def isPalindromeNumber(n):
    n_str = str(n) #convert to str to more easily access each digit in the number

    #we will compare pairs of numbers (1st and last, 2nd and 2nd last, etc).
    #if the value is even, we will check each of these pairs.
    #but if the value is odd, we dont need to check the middle number as it doesnt have a pair.

    if len(n_str) % 2==0: #if value is even
        range_value = len(n_str) / 2 #there will be length of number / 2 pairs to check
    else:
        range_value = (len(n_str) -1) /2 #if it is odd, there will be (length of # -1)/2 pairs to check

    for i in range(   int(range_value)  ): #for each pair of numbers
        if n_str[i] != n_str[len(n_str) -1 -i]: #if any is not equal,
            return False #the num is not palindromic
    return True #otherwise, all pairs are equal so the num is palindromic


lst = []
for i in range(100,1000): #for all 3 digit num
    for j in range(100,1000): #for all 3 digit num
        product = i*j #multiply all possible 3 digit nums with each other
        if isPalindromeNumber(product) == True: #if any of the products are palindromic
            lst += [product] #add to lst

print(max(lst)) #return the maximum value of the list
