# Given two numbers, find the gcd without using inbuilt function
# Example: a = 56, b = 98
# Logic: using --> dividend = divisor*quotient + remainder

# 98 = 56*1 + 42
# 56 = 42*1 + 14
# 42 = 14*3 + 0     gcd = 14

def solve(a,b):
    if b > a:
        a, b = b, a
    while b:
        a, b = b, a%b
    return a

print(solve(56,98))
