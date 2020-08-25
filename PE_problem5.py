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

divisible_by = 20


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


print(value)
