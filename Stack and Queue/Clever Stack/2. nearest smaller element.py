# Given array, find the nearest smaller element A[j] for each element such that j < i
# if there is no smaller element then -1
# Example : A = [4, 5, 2, 10, 8]     ans = [-1, 4, -1, 2, 2]
# Explanation: for element 4, there is no A[j] such tha j < i and A[j] < A[i] so -1
# for ele 5, A[0] < A[1], so 4
# for ele 2, there is no A[j] such tha j < i and A[j] < A[i] so -1
# for ele 10, A[2] < A[3] --> 2 < 10, so 2
# for ele 8, A[2] < A[4] --> 2 < 8, so 2            ans = [-1, 4, -1, 2, 2]

# Simple solution: use two loops, one to iterate every element and other start from i to 0
# and find smaller element 

def prevSmaller(arr):
    ans = [-1 for i in range(len(arr))]
    for i in range(len(arr)):
        for j in range(i-1, -1, -1):
            if arr[j] < arr[i]:
                ans[i] = arr[j]
                break
    return ans

arr = [4, 5, 2, 10, 8]
print(prevSmaller(arr))

# Approach 2: using stack, i from 0 to len(arr)
# i)   keep popping from stack untill if top element >= arr[i] and stack is not empty
# ii)  if stack is not empty, top element is smaller element, else there exist no element
# iii) push in stack

def prevSmaller(arr):
    stack = []
    ans = []
    for i in range(len(arr)):
        while stack and stack[-1] >= arr[i]:
            stack.pop()
        if not stack:
            ans.append(-1)
        else:
            ans.append(stack[-1])
        
        stack.append(arr[i])
    return ans

print(prevSmaller(arr))
