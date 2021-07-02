# Given binary tree, return preorder traversal without using recursion

#            22
#          /    \
#         15     26
#        /  \    / \  
#       12  18  23  28 
#           / \ 
#          16 19
#
# return : [22, 15, 12, 18, 16, 19, 26, 23, 28]

class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

# solve it using stack. store root in stack before loop
# pop from stack and store in result
# then append right node before left node in stack

# Note: append left node after right because when we pop from stack, we get left node
# and for preorder we need (Root Left Right)

class Solution:
    def preorder(self, root):
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)
            
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            
        return result


node = TreeNode(22)
l = TreeNode(15)
ll = TreeNode(12)
lr = TreeNode(18)
lrl = TreeNode(16)
lrr = TreeNode(19)
r = TreeNode(26)
rl = TreeNode(23)
rr = TreeNode(28)

node.left = l
node.right = r
l.left = ll
l.right = lr
lr.left = lrl
lr.right = lrr
r.left = rl
r.right = rr

sol = Solution()
print(sol.preorder(node))
