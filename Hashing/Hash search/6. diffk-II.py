# Given array of integer and a non -ve int k, find if there exist i, j such that
# arr[i] - arr[j] = k, i != j

# Method 1: sort the array and then using two pointers check if arr[i] - arr[j] = k
def solve(arr, k):
    arr.sort()
    i = 0
    j = 1
    while i < len(arr) and j < len(arr):
        if i != j and abs(arr[i] - arr[j]) == k:
            return 1
        elif abs(arr[i] - arr[j]) < k:
            i += 1
        else: 
            j += 1
    return 0

arr = [90, 70, 20, 80, 50]
k = 45
print(solve(arr,k))


# Method 2: using hash table
# iterate through array and check if arr[j] - k or arr[j] + k is present 
# in hash table or not. if not, then add in table 
def solve(arr, k):
    table = set()
    for num in arr:
        if num - k in table or num + k in table:
            return 1
        else:
            table.add(num)

    return 0
    
print(solve(arr,k))
