# reverse the number: 123 --> 321, Return 0 if the result overflows 
# and does not fit in a 32 bit signed integer

def reverse(num):
    rev, n = 0, num
    while n > 0:
        rev = rev*10 + n % 10
        n = n//10
    return rev

def solve(A):
    sign = -1 if A < 0 else 1
    num = abs(A)
    rev = reverse(num)
    if rev > 2**32 -1:
        return 0
    else:
        return sign*rev

print(solve(-12843))
