# Given a number A in a form of string. You have to find the smallest number
# that has same set of digits as A and is greater than A. If A is the greatest
# possible number with its set of digits, then return -1.

# this question is similar to next permutation in array section
# we'll use same logic

def solve(A):
    A = [i for i in A]
    n = len(A)
    pivot_indx = -1
    for i in range(n-2,-1,-1):
        if A[i] < A[i+1]:
            pivot_indx = i
            break
    if pivot_indx == -1:
        return -1
    
    for j in range(n-1, pivot_indx, -1):
        if A[j] > A[pivot_indx]:
            A[j], A[pivot_indx] = A[pivot_indx], A[j]
            break
    reverse_suffix = list(reversed(A[pivot_indx+1:]))
    A = A[:pivot_indx+1] + reverse_suffix
    return int(''.join(A))


print(solve('143876'))