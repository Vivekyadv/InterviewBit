# Given n non-negative integers a1, a2, ..., an,
# where each represents a point at coordinate (i, ai).
#'n' vertical lines are drawn such that the two endpoints of line 
# i is at (i, ai) and (i, 0). that means height is ai from x axis
# Find two lines, which together with x-axis forms a container, 
# such that the container contains the most water.



# Approach: use two pointers i --> start and j --> end of array
# if value at i index < value at j index: i ++   else: j --
# update the max area --> max_area = max(max_area, height*width)
# height = min(arr[i], arr[j]) and width = j-i

def maxArea(arr):
    max_area = i = 0
    j = len(arr)-1
    while i < j:
        height = min(arr[i], arr[j])
        width = j-i
        max_area = max(max_area, height*width)

        if arr[i] < arr[j]:
            i += 1
        else:
            j -= 1
    return max_area

arr = [10,7,12,6,3,12,8,6]
# arr = [6,4,7,3,2,7,5,3]
print(maxArea(arr))
