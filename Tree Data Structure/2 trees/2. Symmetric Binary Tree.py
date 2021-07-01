#Given a binary tree, check whether it is a mirror of itself 
# (ie, symmetric around its center).

#      1
#     / \
#    2   2          this is symmetric around its root node (its center)
#   / \ / \
#  3  4 4  3


class TreeNode:
    def __init__(self, x) -> None:
        self.val = x
        self.left = None
        self.right = None

# Conditions to avoid TLE:
# 1. define check func before main func
# 2. do not use (if not a and not b)
# 3. do not use (if a and b)

class Solution:
    def check(self, a, b):
        if a is None and b is None:
            return 1
        if a is not None and b is not None:
            if a.val == b.val:
                return self.check(a.left, b.right) and self.check(a.right, b.left)
        return 0

    def isSymmetric(self, root):
        return self.check(root, root)
    

    # Method 2: check the false condition
    def check2(self, a, b):
        if not a and not b:
            return 1
        if (not a and b) or (a and not b) or (a.val != b.val):
            return 0
        return (self.check2(a.left, b.right) and self.check2(a.right, b.left))

    def isSymmetric2(self, root):
        return self.check2(root, root)

node = TreeNode(22)
l = TreeNode(20)
ll = TreeNode(12)
lr = TreeNode(15)
r = TreeNode(20)
rl = TreeNode(15)
rr = TreeNode(12)


node.left = l
node.right = r
l.left = ll
l.right = lr
r.left = rl
r.right = rr

a = Solution()
print(a.isSymmetric(node))