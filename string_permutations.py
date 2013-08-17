'''
String Permutations - CodeEval
https://www.codeeval.com/open_challenges/14/


Write a program to print out all the permutations of a string in alphabetical order.

Input sample:

The first argument will be a text file containing an input string, one per line. e.g. 

hat
Output sample:

Print to stdout, permutations of the string, comma separated, in alphabetical order.
e.g.

aht,ath,hat,hta,tah,tha
'''

import sys

def perm(letters):
    #base case
    result = []
    if len(letters) <= 1:
        return letters
    #recursive step
    for i, letter in enumerate(letters):
        for each_perm in perm(letters[:i] + letters[i+1:]):
            result.append(letter + each_perm)
    return result

with open(sys.argv[1]) as f:
    for line in f:
        if line:
            permutations = perm(line.rstrip())
            print ','.join(sorted(permutations))

