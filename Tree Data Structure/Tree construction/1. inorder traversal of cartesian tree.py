# Given inorder traversal of cartesian tree, construct the tree.
# Cartesian tree is a max heap, where root is greater than all elements of subtree

# inorder = [6, 8, 4, 10, 2, 9, 5]
#        10
#      /    \
#     8      9
#    / \    / \
#   6   4  2   5


class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

def buildTree(arr):
    if len(arr) == 0:
        return None
    
    # indx = -1
    # maxVal = -float('inf')
    
    # for i in range(len(arr)):
    #     if arr[i] > maxVal:
    #         maxVal = arr[i]
    #         indx = i

    maxVal = max(arr)
    indx = arr.index(maxVal)
    
    root = TreeNode(maxVal)
    root.left = buildTree(arr[:indx])
    root.right = buildTree(arr[indx+1:])
    
    return root


# Method 2: using stack
def buildTree(A):
    stack = []
    last = None
    for num in A:
        node = TreeNode(num)
        while stack and stack[-1].val < node.val:
            last = stack.pop()
        if stack:
            stack[-1].right = node
        if last:
            node.left = last
        stack.append(node)
        last = None
    return stack[0]