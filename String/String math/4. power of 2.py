# Find if Given number is power of 2 or not.
# More specifically, find if given num can be expressed as 2^k where k >= 1.

# Method 1: using log func
# 2 ^ k = num
# k*log(2) = log(num)
# k = log(num,2)
# if ceil value of k is equal to k then it can be expressed

num1 = "1024"
num2 = "1023"

from math import log, ceil
def power(num):
    num = int(num)
    if num < 2:
        return 0
    k = log(num,2)
    return 1 if ceil(k) == k else 0

print(power(num1), end= ' ')
print(power(num2))

# Method 2: divide num in loop and check if its completely divisible by 2
def power(num):
    num = int(num)
    if num < 2:
        return 0
    
    while num != 1:
        if num % 2 == 0:
            num = num//2
        else:
            return 0
    return 1

print(power(num1), end= ' ')
print(power(num2))

# Method 3: using bitwise & operator
# Logic: If we subtract a power of 2 numbers by 1 then all unset bits 
# after the only set bit become set; and the set bit becomes unset.

# Example: 16 (10000) and 15 (01111) --> bitwise and of 16 and 15
# is 00000 i.e 0

# Time Complexity: O(1)
def power(num):
    num = int(num)
    if num == 1 :
        return 0
    if num & (num-1) == 0:
        return 1
    else:
        return 0

print(power(num1), end= ' ')
print(power(num2))

# Method 4: if num is power of 2, then no_of bit 1 is equal = 1
def power(num):
    num = int(num)
    bin_num = bin(num)
    if bin_num.count('1') == 1:
        return 1
    else: 
        return 0

print(power(num1), end= ' ')
print(power(num2))