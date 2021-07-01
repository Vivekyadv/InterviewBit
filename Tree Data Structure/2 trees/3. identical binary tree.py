# Given two Binary Trees. check if they are identical or not
# Identical: have same structure and the nodes have same values
 

class TreeNode:
    def __init__(self, x) -> None:
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, a, b):
        if not a and not b:
            return 1
        if (not a or not b) or (a.val != b.val):
            return 0

        leftCheck = self.isSameTree(a.left, b.left)
        rightCheck = self.isSameTree(a.right, b.right)

        return leftCheck and rightCheck

    def isSameTree(self, a, b):
        if not a and not b:
            return 1
        if a and b:
            if a.val == b.val:
                leftCheck = self.isSameTree(a.left, b.left)
                rightCheck = self.isSameTree(a.right, b.right)
                return leftCheck and rightCheck
        return 0


# Tree 1
node1 = TreeNode(22)
l = TreeNode(20)
ll = TreeNode(12)
lr = TreeNode(15)
r = TreeNode(20)

node1.left = l
node1.right = r
l.left = ll
l.right = lr

# Tree 2
node2 = TreeNode(22)
l_ = TreeNode(20)
ll_ = TreeNode(12)
lr_ = TreeNode(15)
r_ = TreeNode(2)

node2.left = l_
node2.right = r_
l_.left = ll_
l_.right = lr_
a = Solution()
print(a.isSameTree(node1, node2))