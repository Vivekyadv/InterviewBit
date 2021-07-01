# Given two binary tree A and B. merge them in single binary tree
# The merge rule is that if two nodes overlap, then sum of node values is the new value 
# of the merged node. Otherwise, the non-null node will be used as the node of new tree.
#   Tree 1     Tree 2         Merged Tree

#      2            3               5
#     / \          / \             / \
#    1   4    +   6   1    -->    7   5
#   /              \   \         / \   \
#  5                2   7       5   2   7  

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Method 1: merge tree b in tree a and return a
    def merge(self, a, b):
        a.val = a.val + b.val
        if a.left and b.left:
            self.merge(a.left, b.left)
        if a.right and b.right:
            self.merge(a.right, b.right)
        if not a.left and b.left:
            a.left = b.left
        if not a.right and b.right:
            a.right = b.right

    def mergeTree1(self, a, b):
        if not a:
            return b
        elif b:
            self.merge(a, b)
        return a

    # Method 2: create new tree and merge a and b
    def mergeTree2(self, a, b):
        if not a and not b:
            return None
        if a and not b:
            return a
        if b and not a:
            return b
        
        root = TreeNode(a.val + b.val)
        root.left = self.mergeTree2(a.left, b.left)
        root.right = self.mergeTree2(a.right, b.right)

        return root
    
    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)
        print(node.val, end=' ')
        self.inorder(node.right)


node1 = TreeNode(2)
l = TreeNode(1)
ll = TreeNode(5)
r = TreeNode(4)

node1.left = l
node1.right = r
l.left = ll

# Tree 2
node2 = TreeNode(3)
l_ = TreeNode(6)
lr_ = TreeNode(2)
r_ = TreeNode(1)
rr_ = TreeNode(7)

node2.left = l_
node2.right = r_
l_.right = lr_
r_.right = rr_

sol = Solution()
newTree = sol.mergeTree2(node1, node2)
sol.inorder(newTree)