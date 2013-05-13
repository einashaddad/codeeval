"""

Write a program to determine the sum of the first 1000 prime numbers.

Input sample:

None

Output sample:

Your program should print the sum on stdout.i.e.

3682913
"""

def is_prime(n):
    ''' if divisible by anything other than 1 and itself, return True'''
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = 2
primes = []
while len(primes) < 1000:
    if is_prime(n):
        primes.append(n)
    n += 1

print sum(num for num in primes)

