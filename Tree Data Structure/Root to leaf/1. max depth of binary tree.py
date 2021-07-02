# Given a Binary Tree, find its max depth

#      2        height of root 2 =  1 + max(LST, RST) --> 1 + max(2,2)
#     / \                   
#    1   4      height of 1 = 1 + max(1,0) , height of 4 = 1 + max(1,1)
#   /   / \       
#  5   8  10    height of 5, 8 or 10 = 1 + max(0,0) 


# Algorithm:
# if root is empty, return 0
# left = call func on left subtree recursively
# right = call func on right subtree recursively
# return 1 + max(left, right)

def maxDepth(root):
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))
