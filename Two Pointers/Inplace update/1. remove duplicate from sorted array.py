# Given sorted array, remove duplicate in place such that each ele 
# can appear atmost twice and return its length. 
# Note: Do not allocate extra space for another array


# Method 1: take 2 pointers i = 0 and j = 1. run loop while j < len(arr)
# find next num (diff from arr[i]) and store it in arr[i+1]
# after loop, arr till i+1 will be ans
def solve(arr):
    i = 0
    j = i+1
    while j < len(arr):
        if arr[i] == arr[j]:
            j += 1
        else:
            arr[i+1] = arr[j]
            i += 1
            j += 1
    arr[:] = arr[:i+1]
    return i+1, arr

arr = [1,1,1,2,2,3,5,8,8,8,11,13,15,15,17]
print(solve(arr))

# swap the next diff number. 
def solve(arr):
    i, j = 0, 1
    while j < len(arr):
        if arr[i] == arr[j]:
            j += 1
        else:
            arr[i+1], arr[j] = arr[j], arr[i+1]
            i += 1
            j += 1
    arr = arr[:i+1]
    return i+1, arr

arr = [1,1,2,3,5,5,5,7,8,8,11,12]
print(solve(arr))

# def solve(arr): 
#     q = 0
#     t = 1
#     for i in range(1,len(arr)):
#         if arr[i] != arr[q]:
#             q = t
#             arr[i], arr[t] = arr[t], arr[i]
#             t += 1
#     arr = arr[:q+1]
#     return q+1, arr

# arr = [1,1,2,3,5,5,5,5,8,8,11,12]
# print(solve(arr))