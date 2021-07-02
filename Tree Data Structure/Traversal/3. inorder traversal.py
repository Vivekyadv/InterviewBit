# Given binary tree, return inorder traversal without using recursion

#            22
#          /    \
#         15     26
#        /  \    / \  
#       12  18  23  28 
#           / \ 
#          16 19
#
# return : [12, 15, 16, 18, 19, 22, 23, 26, 28]

class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

# Solve inorder using stack (inorder: Left Root Right)
# if node is not None, push in stack and move left
# if not is None: pop from stack, store in result and move right

class Solution:
    def inorder(self, root):
        stack = []
        result = []
        while stack or root:
            # if root is not None, append in stack and move left
            if root:
                stack.append(root)
                root = root.left
            
            # if root is None and stack is not empty, store popped element 
            # in result and move right
            elif stack:
                root = stack.pop()
                result.append(root.val)
                root = root.right

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
print(sol.inorder(node))