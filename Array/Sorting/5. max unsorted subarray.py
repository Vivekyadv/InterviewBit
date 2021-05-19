# Given array of int A0..A1..A2......An-1
# find min subarray Al..Al+1..Al+2.....Ar, such that if we sort this
# subarray then whole array will be sorted

def solve(A):
    sort_arr = sorted(A)
    if A == sort_arr:
        return [-1]
    else:
        sub_arr = [i for i in range(len(A)) if A[i] != sort_arr[i]]
        return [min(sub_arr), max(sub_arr)]


arr = [1,2,4,3,7,6,5,10,9,8]
arr2 = [ 1, 1, 10, 10, 15, 10, 15, 10, 10, 15, 10, 15, 18 ]
print(solve(arr2))


def solve2(A):
    start = end = -1
    n = len(A)
    for i in range(n-1):
        if A[i] > A[i+1]:
            start = i
            break
    if start == -1:
        return [-1]

    for j in range(n-1,0,-1):
        if A[j-1] > A[j]:
            end = j
            break
    
    minval = min(A[start:end+1])
    maxval = max(A[start:end+1])

    for i in range(start):
        if A[i] > minval:
            start = i
            break
    
    for j in range(n-1,end,-1):
        if A[j] < maxval:
            end = j
            break
    
    return [start,end]

print(solve2(arr2))
