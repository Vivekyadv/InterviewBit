def largestRectangleArea(arr):
    i, n = 0, len(arr)
    stack = []
    max_area = 0
    while i < n :
        if not stack or arr[stack[-1]] <= arr[i] :
            stack.append(i)
            i += 1
        else :
            top = stack.pop()
            area = (arr[top])*(i - stack[-1] - 1 if stack else i)
            max_area = max(max_area, area)
        
    while stack :
        top = stack.pop()
        area = (arr[top])*(i - stack[-1] - 1 if stack else i)
        max_area = max(max_area, area)
    
    return max_area

arr = [ 90, 58, 69, 70, 82, 100, 13, 57, 47, 18 ]
arr = [2,1,5,6,2,3]
print(largestRectangleArea(arr))

def largestRectangleArea(arr):
    stack = []
    n = len(arr)
    left = [-1 for i in range(n)]
    right = [-1 for i in range(n)]

    for i in range(n):
        if not stack:
            # if stack is empty, store 0 in left and append current index in stack
            left[i] = 0
            stack.append(i)
        else:
            # if stack is not empty, pop element untill arr[top] < arr[i]
            # now if stack is empty, store 0 in left else store top + 1
            # and append current index in stack
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            left[i] = 0 if not stack else stack[-1] + 1
            stack.append(i)

    # we can use another stack for right indices, or we can reuse original stack
    while stack:
        stack.pop()

    for i in range(n-1,-1,-1):
        if not stack:
            # if stack is empty, store n-1 in right and append current index
            right[i] = n-1
            stack.append(i)
        else:
            # if stack is not empty, then pop untill arr[top] < arr[i]
            # now if stack is empty, store n-1 in right else store top - 1
            # and append current index
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            right[i] = n-1 if not stack else stack[-1] - 1 
            stack.append(i)

    # now calculate width of rectangle and calc area
    max_area = 0
    for i in range(n):
        width = right[i] -left[i] + 1
        max_area = max(max_area, width * arr[i])
    return max_area 

print(largestRectangleArea(arr))


def editorial(height):
    height.append(0)
    stack = [-1]
    ans = 0
    for i in range(len(height)):
        while height[i] < height[stack[-1]]:
            h = height[stack.pop()]
            w = i - stack[-1] - 1
            ans = max(ans, h*w)
        stack.append(i)
    height.pop()
    return ans

print(editorial(arr))