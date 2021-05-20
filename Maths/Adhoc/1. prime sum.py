# Given an even number, return two prime numbers whose sum
# is equal to given number
# Logic: check i and num-i is prime or not

from math import sqrt

def isPrime(n):
    if n == 2: return True
    if n % 2 == 0:
        return False

    for i in range(3, int(sqrt(n) +1), 2):
        if n % i == 0:
            return False
    return True

def primeSum(num):
    for i in range(2, num//2 +1):
        p1 = i
        p2 = num - i
        if isPrime(p1) and isPrime(p2):
            return [p1,p2]
    return "Not possible"

print(primeSum(12))
