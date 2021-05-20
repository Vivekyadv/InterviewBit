# Rearrange array so that Arr[i] becomes Arr[Arr[i]] with O(1) extra space.
# array contains elements between 0 to n-1, n = size of array, 

def arrange(A):
    n = len(A)
    for i in range(n):
        A[i] = A[i] + (A[A[i]] % n) * n
    for i in range(n):
        A[i] = A[i]// n
    return A

arr = [0,2,4,3,1]
print(arrange(arr))