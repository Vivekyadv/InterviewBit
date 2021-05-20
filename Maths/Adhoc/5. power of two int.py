# Given a num, find if it can be expressed as A^P, where P > 1
# and A > 0. A and P both should be integer

# Logic: take log of num with base A 
#        P = log(num) / log(A)

# Logic 2: take inverse power of given number


from math import sqrt, log

def solve(num):
    for a in range(2, int(sqrt(num)) + 1):
        p = int(log(num,a))
        if a ** p == num:
            return True
    return False

def solve2(num):
    for p in range(2, int(sqrt(num)) + 1):
        a = num ** (1/p)
        if a ** p == num:
            return True
    return False

