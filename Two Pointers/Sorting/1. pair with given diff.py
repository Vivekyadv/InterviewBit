# Given 1-D unsorted array having n integers, find if there exists a pair
# whose difference is B
# Example: arr = [5, 10, 3, 2, 50, 80]      B = 78
# pair = (80,2)

# Method 1: Brute-force method
def solve(arr, B):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            diff = arr[j] - arr[i]
            if diff == B:
                # pair = (arr[j], arr[i])
                return 1
    return 0

arr = [5,10,3,2,50,80]
print(solve(arr, 78))

# Method 2: store uniq_ele (unique elements) of array and check for 
# each element in array if there is arr[i] + x present in uniq_ele 
def solve_set(arr, x):
    res = set()
    for i in range(len(arr)):
        if (arr[i] + x) in res or (arr[i] - x) in res:
            return 1
        else:
            res.add(arr[i])
    return 0

arr = [-2, -1, 7, -4, 12, 6, 18, 11, 13, -10]
x = -4
print(solve_set(arr,x))



# Method 3: sort array and then using 2 pointers, find if pair is present
# Step 2: take 2 pointers, i = 0 and j = 1. Now in linear loop, check 
# if difference of arr[j] and arr[i] > B:
#     i += 1
# if arr[j] - arr[i] < B:
#     j += 1
# else: element found

def solve_abs(arr, x):
    arr.sort()
    x = abs(x)
    i, j = 0, 1
    while j < len(arr):
        if i != j and abs(arr[j] - arr[i]) == x:
            return 1
        elif abs(arr[j] - arr[i]) > x:
            i += 1
        else: # arr[j] - arr[i] < x
            j += 1
    return 0

print(solve_abs(arr, x))
