# Given a Binary Tree and a key. You need to find a path from root to key
# Note: This may be or may be not BST
#          22
#        /    \
#      20      24               target = 25, path = [22, 24, 26, 25]
#     /  \    /  \
#    12  15  23  26
#               /  \
#              25  30



# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    # @param root : root node of tree
    # @param target : integer
    # @return a list of integers     
    def solve(self, root, target):
        path, tempList = [], []

        def findPath(root, target, tempList):
            if not root:
                return None
            if root.val == target:
                tempList.append(root.val)
                path[:] = tempList
            root.left = findPath(root.left, target, tempList+[root.val])
            root.right = findPath(root.right, target, tempList+[root.val])
        
        findPath(root, target, tempList)
        return path


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
print(sol.solve(node, 25))




# same approach different code

def findPath(self,root,target,path):
    if not root:
        return None
    if root.val == target:
        return path+[root.val]
    
    left = self.findPath(root.left,target,path+[root.val])
    if left:
        return left

    right = self.findPath(root.right,target,path+[root.val])
    if right:
        return right

    if not left and not right:
        return None
        
def solve(self, root, target):
    return self.findPath(root,target,[])


# Solution 2
def __init__(self):
    self.path=list()
    
def solve(self, root, target):
    if self.findPath(root,target):
        return self.path
        
def findPath(self,root,target):
    if not root:
        return False
    
    self.path.append(root.val)
    if root.val==target:
        return True
    
    left = self.findPath(root.left,target)
    right = self.findPath(root.right,target)

    # check on left subtree and right subtree, if anyone gives True
    # that means path exist
    if left or right:
        return True
    
    self.path.pop()
    return False