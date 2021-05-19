from collections import Counter

def Count(A):
    counter = dict()
    for ele in A:
        if ele in counter:
            counter[ele] += 1
        else:
            counter[ele] = 1
        
    return f'Counter {counter}'


# method 1: using sum(array), sum of range 
#           (sum of array should be sum of range)

def solve(A):
    n = len(A)
    repeat = sum(A) - sum(set(A))
    sum_of_range = n*(n+1)//2
    missing = sum_of_range - sum(A) + repeat
    return [repeat, missing]


# method 2: using collections.Counter()

def solve2(A):
    n = len(A)
    count = Counter(A)
    for i in range(1, len(A)+1):
        if count[i] > 1:
            repeat = i
        elif count[i] == 0:
            missing = i
    return [repeat, missing]

def solve3(A):
    n = len(A)+1
    count = [0]*n
    for ele in A:
        count[ele] += 1

    for i in range(1,n):
        if count[i] > 1:
            repeat = i
        elif count[i] == 0:
            missing = i
    return [repeat, missing]

print(solve([3,1,2,5,3]))
ar = [1,2,3,4,5,4,7,8]
print(solve(ar))
print(solve2(ar))
print(solve3(ar))
