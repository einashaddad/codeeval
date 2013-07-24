'''
Reverse and Add - CodeEval
https://www.codeeval.com/open_challenges/45/

Choose a number, reverse its digits and add it to the original. 
If the sum is not a palindrome (which means, it is not the same 
number from left to right and right to left), repeat this procedure.
'''

import sys

def reverse_and_add(n, count=0):
    if count >= 1000:
        return None
    n = str(n)
    length = len(n)
    for i in xrange(length/2):
        if n[i] != n[length-i-1]:
            n2 = n[::-1]
            count += 1
            return reverse_and_add(int(n)+int(n2), count)
    print count, n

with open(sys.argv[1]) as f:
    for number in f:
        reverse_and_add(number)

