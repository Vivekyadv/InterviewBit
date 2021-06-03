# Given integer n, find total of set bits from 1 to n
# num = 3 ::: 001, 010, 011 = total set bits = 4

# Approach 1: count total bits at each position
# 2 1 0 -- position
# 0 0 1 -- 1
# 0 1 0 -- 2        count bits at pos 0 = 2, at pos 1 = 2
# 0 1 1 -- 3
def totalBits(num):
    mod = pow(10,9) + 7
    count = 0
    for i in range(32):
        for j in range(1,num+1):
            if j & 1<<i:
                count += 1
    return count % mod

num = 10
print(totalBits(num))

# Time complexity: O(32*n)
# Gives TLE for larger case

# Approach 2: count set bits of every number in its binary form
# either use bin(x).count('1') or use & operator 
def count1bits(x):
    bits = 0
    while x > 0:            # while x > 0:
        if x % 2 == 1:          # x = x & (x-1)
            bits += 1           # bits += 1
        x = x//2            # return bits
    return bits

def totalBits(num):
    setbits = 0
    for i in range(num+1):
        setbits += count1bits(i)
    return setbits

print(totalBits(num))

# Approach 3: find 2^i which is just smaller than given number
# if we observe. from 0 to 2^i there are i*pow(2,i-1) set bits
# now remaining number (x) = num - 2^i, in these numbers, there are x+1
# set bits at last pos (most significant bit)
# solve remaining bits using recursion 

def solve(num):
    mod = 10**9 + 7
    if num <= 0:
        return 0
    i = ans = 0
    while 1<<i <= num:
        i += 1
    i = i-1
    ans += i * pow(2,i-1) + (num-pow(2,i) + 1) + solve(num-pow(2,i))
    return int(ans) % mod

print(solve(num))
