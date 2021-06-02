# Reverse the bits of 32 bit unsigned int
# Example : 3 
#               00000000000000000000000000000011    
# reversed =>   11000000000000000000000000000000 --> 3221225472


# Method 1: convert to binary, reverse it and then again convert to int
def reverse(num):
    num = bin(num)[2:]
    num = '0'*(32-len(num)) + num
    rev_num = num[::-1]
    return int(rev_num, 2)

print(reverse(7))

# Method 2: 

def reverse(num):
    ans=0
    n = 32
    for i in range(n) :
        # we can use (1 << i) & num ::or:: (num >> i) & 1
        if (num >> i) & 1:
            ans = ans | 1 << (n-1-i)
        
    return ans

print(reverse(7))
