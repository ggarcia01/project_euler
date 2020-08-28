'''
garcia, gil
created: 8/28/2020
last updated: 8/28/2020

project euler problem #8 description:


The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

731671765...
...
...
...
...963450

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
What is the value of this product?
'''


digit_str = """73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450"""


num_of_adjacent_digits = 13



def greatestProductOfAdjacentDigist(num_of_adjacent_digits=num_of_adjacent_digits, digit_str = digit_str):
    # we are going to convert our string to a list of the digits
    digit_lst = []
    for element in digit_str:
        #from the way we inputed our digit_str, there are '\n' dilimeters that we need to get rid of
        if element != '\n':
            digit_lst += [int(element)] #add only the digits as integers to our list

    #initializing our start and end index, which we will be updating by 1 each cycle
    start_index = 0
    end_index = start_index + num_of_adjacent_digits
    #initializing the biggest product which will be updated every time a bigger product is produced
    biggestProd = 0
    #initializing a variable where the digits that produced the biggest product will be stored
    digits_producing_biggest_prod = None
    while end_index < len(digit_lst): #testing every possible set of adjacent digits
        prod = 1 #initializing the product value that will be calcuated for each set
        digit_slice = digit_lst[start_index:end_index] #indexing to the next set
        for i in digit_slice:
            prod *= int(i) #multiply each element in the set
        if prod > biggestProd: #if the result is bigger than the biggest product produced thus far
            biggestProd = prod #replace it
            digits_producing_biggest_prod = digit_slice #update the digit slice to the new set that produced the biggest product
        #update the start and end index by 1
        start_index += 1
        end_index += 1
    return biggestProd,digits_producing_biggest_prod




biggest_product, digits_producing_biggest_product = greatestProductOfAdjacentDigist(num_of_adjacent_digits)
print(biggest_product,digits_producing_biggest_product)
