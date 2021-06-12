# Given array of non -ve integers represents the height of building.
# compute how much water it is able to trap after raining


# Approach: for every element of given array, find highest building on the left
# and highest on the right. Take the smaller of two heights.
# The difference btw smaller height and heigt of current element is the amount of water
# can be stored by that building

# Maintain two arrays, left_max & right_max and calculate using above approach 
def trap_water(arr):
    n = len(arr)
    water = 0
    
    left_max = [0 for i in range(n)]
    right_max = [0 for i in range(n)]
    
    left_max[0] = arr[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], arr[i])
    
    right_max[-1] = arr[-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], arr[i])
    
    for i in range(n):
        water += min(left_max[i], right_max[i]) - arr[i]
    
    return water

arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap_water(arr))

# Time and Space complexity: O(n)

# Approach 2: instead of maintaining two arrays, maintain two variables to store the 
# maximum till that point

def trap_water(arr):
    water = 0
    left_max = right_max = 0

    low = 0
    high = len(arr) -1

    while low <= high:
        if arr[low] < arr[high]:
            if arr[low] > left_max:
                left_max = arr[low]
            else:
                water += left_max- arr[low]
            low += 1

        else:
            if arr[high] > right_max:
                right_max = arr[high]
            else:
                water += right_max- arr[high]
            high -= 1
    return water

print(trap_water(arr))
