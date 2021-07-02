# Given Binary Tree, find its minimum depth
#          22
#        /    \
#      20      24   
#             /  \
#           23    26


class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    def minDepth(self, root):
        if not root:
            return float('inf')
        if root.left is None and root.right is None:
            return 1
        
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

    def minDepth2(self, root, level):
        if root is None:
            return level
        level += 1
        return min (self.minDepth2(root.left, level), self.minDepth2(root.right, level))
    
    def minDepth3(self, root):
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            return 1
        
        if not root.left:
            return self.minDepth3(root.right) + 1
        
        if not root.right:
            return self.minDepth3(root.left) + 1
        
        return 1 + min(self.minDepth3(root.left), self.minDepth3(root.right))


node = TreeNode(22)
l = TreeNode(20)
r = TreeNode(24)
rl = TreeNode(23)
rr = TreeNode(26)

node.left = l
node.right = r
r.left = rl
r.right = rr

sol = Solution()
print(sol.minDepth(node))
print(sol.minDepth2(node,0))
print(sol.minDepth3(node))