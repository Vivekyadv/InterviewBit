# Given two integers p, q (numerator and denominator) of fraction. return the fraction in
# string format. If the fractional part is repeating, enclose the repeating part in parentheses.

# Example: 1/2      0.5
#          1/3      0.3333...   -> 0.(3)


# Editorial solution
def fractionToDecimal(A, B):	
    if B == 0:
        return 'ZeroDivisionError'

    retlist = []
    if (A < 0) ^ (B < 0) and (A != 0):
        retlist.append('-')
    A = abs(A)
    B = abs(B)
    retlist.append(str(A//B))
    if A % B:
        retlist.append('.')

    hashmap = {}

    rem = A % B
    while  rem and  rem not in hashmap:
        hashmap[rem] = len(retlist) - 1
        rem = 10 * rem 
        retlist.append(str(rem // B))
        rem = rem % B
    if rem:
        retlist.insert(hashmap[rem]+1, '(')
        retlist.append(')')

    ans = [val for val in retlist]
    return ''.join(ans)


for i in range(10):
    p = 211
    q = i+1
    print(p/q)
    print(fractionToDecimal(p,q))
    print()
