# You are given a preorder traversal A, of a Binary Search Tree.
# Find if it is a valid preorder traversal of a BST.

# Example: arr = [4, 2, 1, 3, 6, 5, 7]
# Tree         4
#            /    \
#           2       6
#          / \     / \
#         1   3   5   7
#                         
#   Preorder traversal:  4-> 2-> 1-> 3-> 6-> 5-> 7
# since given array and preorder traversal are same, return 1


# Method 1: for each element in array, for example current element = 4
# find first element which is > current element (i.e. 6). then check in the right of 6
# if there is any element which is less then curr element (4). if so, return 0
# then recursively do this for all elements in array

def solve(arr):
    for i in range(len(arr)-1):
        curr_node = arr[i]

        for j in range(i+1, len(arr)):
            if arr[j] > curr_node:
                break
        
        j += 1
        while j < len(arr):
            if arr[j] < curr_node:
                return 0
            j += 1    
    return 1

arr = [4, 2, 1, 3, 6, 5, 7]
print(solve(arr))


# Method 2: using stack
# initialise root = -inf, in a loop
# if arr[i] < root, return False
# keep removing element from stack while arr[i] > top of stack. make last removed 
# element as root   -> root = stack.pop(). At this point, arr[i] > removed root
# push arr[i] in stack

def solve(arr):
    stack = []
    root = -float('inf')
    for node in arr:
        if node < root:
            return 0
        while stack and stack[-1] < node:
            root = stack.pop()
        stack.append(node)
    return 1

print(solve(arr))
        
def solve(arr):
    low = -2**32
    high = arr[0]
    for node in arr:  
        if node < low : 
            return 0 
        if node > high:
            low = high
        high = node
    return 1