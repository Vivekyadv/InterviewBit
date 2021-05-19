# Given a num, find if it can be expressed as A^P, where P > 1
# and A > 0. A and P both should be integer


#        A ^ P = num
#        P.log(A) = log(num)
#        P = log(num) / log(A)

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
    
a = 'abc'
b = reversed(a)
for i in b:
    print(i,end=' ')