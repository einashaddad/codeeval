"""
Given a positive integer, find the sum of its constituent digits.

Input sample:

The first argument will be a text file containing positive integers, one per line. e.g. 

23
496
Output sample:

Print to stdout, the sum of the numbers that make up the integer, one per line.
e.g.

5
19
"""

import sys

with open(sys.argv[1]) as f:
    for str_num in f:
        print sum(int(i) for i in str_num if i != '\n')
        