# Given a binary tree, determine if it is height-balanced.
# Height-balanced binary tree : is defined as a binary tree in which the depth of the 
# two subtrees of every node never differ by more than 1.

#         22   
#       /    \    
#      20     24  
#       \       \       Not Balanced
#       15      26  
#               / \
#              25  30

class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

# Method 1: calculate left height and right height of each node and 
# check if it is balanced or not.  
def height(root):
    if not root:
        return 0

    return 1 + max(height(root.left), height(root.right))

class solution:
    # @param A : root node of tree
    # @return an integer
    def isBalanced(self, root):
        if not root:
            return 1
        
        lh = height(root.left)
        rh = height(root.right)

        leftCheck = self.isBalanced(root.left)
        rightCheck = self.isBalanced(root.right)

        if abs(lh-rh) <= 1 and leftCheck and rightCheck:
            return 1
        return 0


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
print(a.isBalanced(node))



# Method depth of node from root, then check if it is balanced or not
ans = 1
def findDepth(self,node,depth):
    if not node:
        return depth-1
        
    left = self.findDepth(node.left,depth+1)
    right = self.findDepth(node.right,depth+1)
    
    if abs(left-right) > 1:
        self.ans = 0
    return max(left, right)
    
def isBalanced(self, root):
    self.findDepth(root,0)
    return self.ans