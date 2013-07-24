'''
Prime Numbers - CodeEval
https://www.codeeval.com/open_challenges/46/

Print out the prime numbers less than a given number N. For bonus points your solution 
should run in N*(log(N)) time or better. You may assume that N is always a positive integer.

'''
import math
import sys 

def prime_numbers(n):
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    return ','.join([str(number) for number in primes])

def is_prime(n):
    '''
    Checking divisibility up to the square root of the number because if n is divisible by i,
    then it is also divisible by n/i
    '''
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True
        
with open(sys.argv[1]) as f:
    for test in f:
        print prime_numbers(int(test))