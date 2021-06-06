# Given array with n objects colored red (0), white(1) or blue(2),
# sort them so that obj of same color are adjacent in order of 
# red, white and blue
# Example: arr = [0 1 2 0 1 2] --> ans = [0 0 1 1 2 2]

# Method 1: count no of red, white and blue objects and then 
# return redCount*[0] whiteCount*[1] blueCount*[2] 
def solve(arr):
    redCount = whiteCount = blueCount = 0
    for val in arr:
        if val == 0:
            redCount += 1
        elif val == 1:
            whiteCount += 1
        elif val == 2:
            blueCount += 1
    result = redCount*[0] + whiteCount*[1] + blueCount*[2]
    return result

arr = [1,0,0,2,2,1,1,0,1,1,0,1,0,2,0,1,0,2,2,2,2,0,1,0,2]
# print(solve(arr))

## above method in lesser lines of code
## redCount = count[0], whiteCount = count[1], blueCount = count[2]
# count = [0,0,0]
# for i in arr:
#     count[i] += 1
# return [0]*count[0] + [1]*count[1] + [2]*count[2]


# Method 2: using 3 pointers::: ptr1 starts from 0 and ptr3 starts
# from end of array. ptr 2 will iterate from ptr1 to ptr3
# if arr[ptr2] == 0: swap(ptr1,ptr2) and ptr1++, ptr2++
# if arr[ptr2] == 2: swap(ptr2, ptr3) and ptr3--
# if arr[ptr2] == 1: ptr2++
def solve(arr):
    i = j = 0
    k = len(arr)-1
    while i <= j <= k:
        if arr[j] == 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
        elif arr[j] == 1:
            j += 1
        else:
            arr[j], arr[k] = arr[k], arr[j]
            k -= 1
    return arr

arr = [2, 1, 0, 2, 2, 0, 2, 1, 1, 0, 1, 1, 2]
print(solve(arr))
