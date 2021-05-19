# Given an even number, return two prime numbers whose sum
# is equal to given number


from math import sqrt

def isPrime(n):
    for i in range(2, int(sqrt(n) +1)):
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
