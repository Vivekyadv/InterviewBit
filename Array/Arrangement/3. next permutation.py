# given integer array A of size N, find the next permutation of number
# 1 2 3 --> 1 3 2 --> 2 1 3 --> 2 3 1 --> 3 1 2 --> 3 2 1 
# and then again 1 2 3

# example: 1 2 5 4 3 --> 1 3 2 4 5 is next permutation

def next_permutation(A):
    n = len(A)

    pivot_indx = -1
    for i in range(n-2,-1,-1):
        if A[i] < A[i+1]:
            pivot_indx = i
            break
    if pivot_indx == -1:
        return A.sort()
    
    for j in range(n-1, pivot_indx, -1):
        if A[j] > A[pivot_indx]:
            A[j], A[pivot_indx] = A[pivot_indx], A[j]
            break
    
    reverse_suffix = list(reversed(A[pivot_indx+1:]))
    A = A[:pivot_indx+1] + reverse_suffix
    return A

arr = [1,2,3,6,5,4,1]
print(next_permutation(arr))