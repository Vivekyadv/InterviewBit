# Given sorted array, convert it to height balanced BST

# Arr = [2, 4, 5, 7, 9, 10, 13]
#          7
#        /  \
#       4    10
#      / \   / \
#     2   5  9  13

# Approach: take middle element of array as root
# left side of mid element is left subtree and right side of mid is right subtree
# call recursively for left subtree and right subtree

class TreeNode:
    def __init__(self, data):
        self.root = data
        self.left = None
        self.right = None

def sortedArrayToBST(arr):
    if len(arr) == 0:
        return None
    
    mid = len(arr)//2
    root = TreeNode(arr[mid])
    root.left = sortedArrayToBST(arr[:mid])
    root.right = sortedArrayToBST(arr[mid+1:])
    
    return root