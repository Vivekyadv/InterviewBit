# Given two binary strings, return their sum (also in string)


# Method 1: convert to int --> add them --> then convert again to binary
def solve(a, b):
    a = int(a, 2)
    b = int(b, 2)
    add = a + b
    return bin(add)[2:]

a = "101011"
b = "100110110"
print(solve(a,b))


# Method 2: simple addition with carry
def solve(a, b):
    len_a = len(a)
    len_b = len(b)

    # make the size of both binary numbers equal
    if len_a < len_b:
        a = '0'*(len_b - len_a) + a
    if len_b < len_a:
        b = '0'*(len_a - len_b) + b
    
    res = ''
    c = 0
    i = len(a)-1
    # now add every bit of a and b
    while i >= 0:
        s = (int(a[i]) + int(b[i]) + c )
        add = s % 2
        c = s // 2

        res = str(add) + res
        i -= 1
    
    if c == 1:
        res = '1' + res
    return res

print(solve(a, b))

# a     --> 000101011
# b     --> 100110110
# sum   --> 101100001
