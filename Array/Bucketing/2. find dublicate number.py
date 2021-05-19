# Given a read only array of n + 1 integers between 1 and n, 
# find one number that repeats

from collections import Counter 
def method1(A):
    A = Counter(A)
    for items in A.keys():
        if A[items] > 1:
            return items
    return -1

ar = [1,2,2,3,4,5,5,7,8,9]
print(method1(ar))


# this function is used when there is only one repeated number
def method2(A):
    n = len(A)
    sum_of_array = sum(A)
    sum_of_range = int(n * (n - 1) / 2)
    ans1 = sum_of_array - sum_of_range

    # when there is one repeated number
    repeat = sum(A) - sum(set(A))
    return ans1, repeat


array = [1,4,3,4,2]
print(method2([1,2,3,4,5,3]))
print(method2(array))


def method3(A):
    n = len(A)+1
    seen = [False]*n
    for i in A:
        if seen[i] == True:
            return i
        else:
            seen[i] = True
    return -1

print(method3([1,2,3,4,5,2,6]))

