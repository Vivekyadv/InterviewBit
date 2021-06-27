# You are given an array of N integers, A1, A2 ,..., AN and an integer B. 
# Return the of count of distinct numbers in all windows of size B.

# Formally, return an array of size N-B+1 where i'th element in this array contains 
# number of distinct elements in sequence Ai, Ai+1 ,..., Ai+B-1.

# Note: if B > N, return an empty array.


def dNums(arr, B):
    res = []
    num_idx = {}
    nSet = None
    lst = []
    if B > len(arr):
        return []
    
    i = 0
    while i < B-1:
        num_idx[arr[i]] = i
        i += 1
        
    while i < len(arr):  
        num_idx[arr[i]] = i
        if i > B-1:
            idx = num_idx[arr[i-B]]
            if idx < i-B+1:
                del num_idx[arr[i-B]]
                
        res.append(len(num_idx))
    
        i += 1
    
    return res

a = [1,2,1,3,4,3]
b = 3
print(dNums(a, b))