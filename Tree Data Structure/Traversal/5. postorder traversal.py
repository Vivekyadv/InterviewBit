# Given binary tree, return preorder traversal without using recursion

#            22
#          /    \
#         15     26
#        /  \    / \  
#       12  18  23  28 
#           / \ 
#          16 19
#
# return : [12, 16, 19, 18, 15, 23, 28, 26, 22]

class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

# Similar to preorder traversal, only difference is that: we push left node and then 
# right node in stack. so after popping, we get (Root Right Left), reverse the result
# after execution of loop. ans = (Left Right Root)
class Solution:
    def postorder(self, root):
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            
        return result[::-1]

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
print(sol.postorder(node))


# node = TreeNode(10)
# l = TreeNode(6)
# r = TreeNode(12)
# rl = TreeNode(11)
# rr = TreeNode(13)

# node.left = l
# node.right = r
# r.left = rl
# r.right = rr