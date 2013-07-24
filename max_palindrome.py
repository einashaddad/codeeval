"""
Prime Palindrome (Difficulty: Easy)

Challenge Description:

Write a program to determine the biggest prime palindrome under 1000.

Input sample:

None

Output sample:

Your program should print the largest palindrome on stdout. i.e.

929
"""
def return_palindrome(max):
    for n in range(max, 0, -1):
        if is_palindrome(str(n)):
            if is_prime(n):
                return n
                
def is_palindrome(number):
    midpoint = len(number)/2
    length = len(number)
    for i in range(0, midpoint):
        if number[i] != number[length-i-1]:
            return False
    return True

def is_prime(n):
    for i in xrange(2, n):
        if n % i == 0:
            return False
    return True
   
print return_palindrome(1000)