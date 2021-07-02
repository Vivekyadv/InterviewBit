# Given a BT and a sum value, determine if the tree has a root to leaf path such that adding
# up all the values along the path equals to given sum
#              5
#             / \
#            4   8              sum = 22,   path = 5->4->11->2. return 0/1
#           /   / \
#          11  13  4
#         /  \      \
#        7    2      1


# Algorithm: if root is none: return 0 (no solution)
# if node is leaf node, then check if node.val == givenSum
# if above condition is false, then check on LST and RST with value of 
# givenSum = givenSum - node.val
# return LST or RST 


class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    def hasPathSum(self, root, givenSum):
        if not root:
            return 0
        
        # if node is a leaf node, then check if node.val == givenSum
        if not root.left and not root.right:
            return 1 if root.val == givenSum else 0
        
        leftCheck = self.hasPathSum(root.left, givenSum-root.val)
        rightCheck = self.hasPathSum(root.right, givenSum-root.val)

        return leftCheck or rightCheck


node = TreeNode(5)
l = TreeNode(4)
r = TreeNode(8)
ll = TreeNode(11)
lll = TreeNode(7)
llr = TreeNode(2)
rl = TreeNode(13)
rr = TreeNode(4)
rrr = TreeNode(1)

node.left = l
node.right = r
l.left = ll
ll.left = lll
ll.right = llr
r.left = rl
r.right = rr
rr.right = rrr

sol = Solution()
print(sol.hasPathSum(node, 18))
