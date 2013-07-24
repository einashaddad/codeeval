import sys

def remove_stutters(test):
    s = { n for n in test }
    if '\n' in s:
        s.remove('\n')
    if ',' in s:
        s.remove(',')
    l = [n for n in s]
    l.sort()
    print ','.join(l) 

with open(sys.argv[1], 'r') as f:
    for test in f:
        remove_stutters(test)
 

#test case: '1,1,1,2,2,3,3,4,4\n'

#hint use while!
