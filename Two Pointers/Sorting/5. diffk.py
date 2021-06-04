# Given sorted array and non -ve int k, find if there exists i and j
# such that arr[i] - arr[j] == k, i != j
# Example: arr= [1,3,5] k = 4 --> and = arr[2]- arr[0] = 4

# Method 1: using nested loop
def solve(arr, k):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if abs(arr[i] - arr[j]) == k:
                return 1
    return 0

arr = [1,3,5]
k = 4
print(solve(arr, k))


# Method 2: use two pointers
# This question is similar to "pair with given diff" 
def solve(arr, k):
    i, j = 0, 1
    while j < len(arr):
        if i != j and abs(arr[j] - arr[i]) == k:
            return 1
        if abs(arr[j] - arr[i]) > k:
            i += 1
        else:
            j += 1
    return 0

arr = [-10, -4, -1, 2, 6, 7, 11, 12, 13, 18]
k = 4
print(solve(arr, k))