# Given Binary Tree with n nodes. Remove all the half nodes and return final Binary Tree
# Half nodes are nodes which have only one child
#
#         22                       22
#       /    \                    /   \
#      20     24       -->       15   26
#       \       \                    /  \
#       15      26                  25  30
#               / \
#              25  30

# node 20 and 24 are half nodes, so remove it from tree

class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class solution:
    def solve(self, root):
        if not root:
            return root
        else:
            # if root.right is None, traverse the root.left using recursion
            if root.left and not root.right:
                return self.solve(root.left)

            # if root.left is None, traverse the root.right using recursion
            if root.right and not root.left:
                return self.solve(root.right)

            # if both are None, it is leaf node, return that node
            root.left = self.solve(root.left)
            root.right = self.solve(root.right)
            return root


node = TreeNode(22)
l = TreeNode(20)
lr = TreeNode(15)
r = TreeNode(24)
rr = TreeNode(26)
rrl = TreeNode(25)
rrr = TreeNode(30)

node.left = l
node.right = r
l.right = lr
r.right = rr
rr.left = rrl
rr.right = rrr

a = solution()
print(a.solve(node))


# Method 2: start from root, if you find any half node, 
# delete it and move its descendants upwards
def solve(root):
    if not root:
        return None
    root.left = solve(root.left)
    root.right = solve(root.right)

    # if both left and right are None, it is leaf node
    if not root.left and not root.right:
        return root

    # if any of left or right is None, it is half node. delete that node
    if not root.left:
        newNode = root.right
        temp = root
        root = None
        del temp
        return newNode

    if not root.right:
        newNode = root.left
        temp = root
        root = None
        del temp 
        return newNode
    
    return root


