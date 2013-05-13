'''
Write a program to determine the Mth to last element of a list.

Input sample:

The first argument will be a text file containing a series of space 
delimited characters followed by an integer representing a index into 
the list(1 based), one per line. e.g. 

a b c d 4
e f g h 2

a b c d 3 = d

Output sample:

Print to stdout, the Mth element from the end of the list, one per line. 
If the index is larger than the list size, ignore that input. 
e.g.

a
g
'''
import sys

def element(series):
    m = int(series[-1])
    l = series[:-1]
    if m <= len(l):
        return l[-m]


with open(sys.argv[1], 'r') as f:
    for series in f:
        print element(''.join(series.split()))
