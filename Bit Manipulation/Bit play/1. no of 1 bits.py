# Given a number, find the no of 1 bits in its binary form
# Example : The 32-bit integer 11 has binary representation
# 00000000000000000000000000001011 --> no of 1 bits = 3

# Method 1: convert it in binary and count no of 1 bits
def numSetBits(num):
    num = bin(num)
    ans = 0
    for i in num[2:]:
        if i == '1':
            ans += 1
    return ans
    # we can also use count() function
    # return num.count('1')

print(numSetBits(1101))

# Method 2: using bitwise & operator
# x-1 will find the '1' bit fron end and set it to '0' and then change 
# all the following bits to '1'
# using this concept we'll increment count 

def numSetBits(num):
    count = 0
    while num > 0:
        num = num & (num-1)
        count += 1
    return count

print(numSetBits(83))


# Method 3:
def numSetBits(num):
    count = 0
    for i in range(0,32):
        b = 1<<i    # 2^i
        a = num & b
        if a:
           count += 1
    return count

print(numSetBits(83))
