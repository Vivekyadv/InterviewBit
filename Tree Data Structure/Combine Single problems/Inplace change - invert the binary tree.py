# Given a binary tree, invert the binary tree and return it.
#      1                    1
#    /   \                /   \
#   2     3       -->    3     2
#  / \   / \            / \   / \
# 4   5 6   7          7   6 5   4


class TreeNode:
    def __init__(self, x) -> None:
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root):
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
    
    def inorder(self, node):
        if not node: return 
        self.inorder(node.left)
        print(node.val, end=' ')
        self.inorder(node.right)


node = TreeNode(22)
l = TreeNode(20)
ll = TreeNode(12)
lr = TreeNode(15)
r = TreeNode(24)
rl = TreeNode(23)
rr = TreeNode(26)
rrl = TreeNode(25)
rrr = TreeNode(30)

node.left = l
node.right = r
l.left = ll
l.right = lr
r.left = rl
r.right = rr
rr.left = rrl
rr.right = rrr

sol = Solution()
print('Original Tree: ', end='')
sol.inorder(node)
print()
n = sol.invertTree(node)
print('Inverted Tree: ', end='')
sol.inorder(n)