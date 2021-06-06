# Given two sorted arrays, find the intersection of both 
# (i.e. common elements of both)

# Method: since arrays are sorted, scan arrays from start
# if arr1[i] == arr2[j] --> this is intersection, store it in result
# if arr1[i] < arr2[j] then inc i. 
# else: inc j
def common(arr1, arr2):
    result = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            result.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    return result

arr1 = [1,2,3,4,5,6]
arr2 = [3,3,4,6]
print(common(arr1, arr2))
