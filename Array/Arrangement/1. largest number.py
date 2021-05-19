# Given a list of non negative integers, 
# arrange them such that they form the largest number.

# Given [3, 30, 34, 5, 9], the largest formed number is 9534330.


def largestNumber(A):
    maxsize = minsize = 1
    for x in A:
        maxsize = max(maxsize,len(str(x)))
        minsize = min(minsize,len(str(x)))
    
    A = map(str, A)
    key = lambda s: s*(maxsize//minsize)
    ans = sorted(A, key=key, reverse = True)
    return str(int(''.join(ans)))

from functools import cmp_to_key as cmp

def largestNumber2(A):
    A = map(str,A)
    key = lambda a,b: 1 if a+b > b+a else -1
    A = sorted(A, key= cmp(key), reverse = True)
    return str(int(''.join(A)))


arr = [3,30,34,5,9]
ans = largestNumber(arr)
ans2 = largestNumber2(arr)
print(ans, type(ans))
print(ans2, type(ans))

