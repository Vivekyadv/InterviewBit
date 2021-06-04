# Given an array, find triplet whose sum is closest to given num X
# arr = [1,2,3,4,-5]    x = 10
# ans = 2+3+4 = 9 closest to 10

# Method 1: sort the array
# fix first element and use two pointers on rest of two elements.
# two pointers --> start = i+1 and end = n-1
# if sum is smaller than target (x) then inc start pointer
# if sum is greater than x, dec end pointer

def solve(arr, target):
    arr.sort()
    n = len(arr)
    closestSum = 2**32-1
    for i in range(n-2):
        start = i+1
        end = n-1
        while start < end:
            add = arr[i] + arr[start] + arr[end]
            if add == target:
                return target
            if abs(target-add) < abs(target-closestSum):
                closestSum = add
            elif add < target:
                start += 1
            else:
                end -= 1
    return closestSum

arr = [ 5, -2, -1, -10, 10 ]
x = 5
print(solve(arr,x))
