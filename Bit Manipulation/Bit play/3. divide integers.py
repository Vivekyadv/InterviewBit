# Divide two integers without using multiplication, division and mod 
# operator. Return the floor of the result of the division.

# Method 1: Keep subtracting the dividend from the divisor until 
# dividend becomes less than divisor. The dividend becomes the remainder, 
# and the number of times subtraction is done becomes the quotient

# pseudo code:
p, q = 43, 8
sign = 1 if (p>0 and q>0) or (p<0 and q<0) else -1
quot = 0
while p > q:
    p -= q
    quot += 1

print(sign * quot)

# Method 2: using bit manipulation to find quotient. calc highest 
# power of 2 such that q * pow(2,x) <= p

# Example:
# 43 = 8*5 + 3      p = 43, q = 8
# 43 = 8 * pow(2,2) + 8 * pow(2,0) + 3
# 43 = 8 * [pow(2,2) + pow(2,0)] + 3
# quotient = pow(2,2) + pow(2,0) ::: in bit form = 1<<2 + 1<<0

def divide(p, q):
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    # if ZeroDivisionError or if dividend > max value
    if q == 0 or (q == 1 and p >= INT_MAX):
        return INT_MAX
    
    # if dividend < min value
    if q == -1 and p <= INT_MIN:
        return INT_MAX

    sign = 1 if (p>0 and q>0) or (p<0 and q<0) else -1
    p = abs(p)
    q = abs(q)

    quot = temp = 0
    for i in range(31,-1,-1):
        if temp + (q<<i) <= p:
            temp += q<<i
            quot += 1<<i
    
    if sign == 1:
        return quot
    else: return -quot