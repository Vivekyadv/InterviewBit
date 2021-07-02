# Given a binary tree and a sum value, find all root-to-leaf path having path 
# sum = given sum value
#              5
#             / \
#            4   8
#           /   / \
#          11  13  4
#         /  \    / \
#        7    2  5   1

# sum value = 22,       return = [5,4,11,2], [5,8,4,5]
# two methods are discussed below

from copy import copy 
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

# Method 1: define func findPath(node, templist, givenSum)
# Step 1: append node.val in templist
# Step 2: if its leaf node and node.val == givenSum, copy templist and store in result
# Step 3: call findPath() in LST, with givenSum reduced by node.val
# Step 4: call findPath() in RST, with givenSum reduced by node.val
# Step 5: after traversing LST and RST, pop top element from templist (for backtracking)

# Note: In Step 2, we can't just result.append(templist) as when the templist changes, 
# it'll also change the list in result. so we need to copy templist and then append(copy)

class Solution:
    def pathSum(self, root, sumVal):
        self.result = []
        templist = []
        if root:
            self.findPath(root, templist, sumVal)
        
        return self.result
        
        
    def findPath(self, node, templist, sumVal):

        templist.append(node.val)

        if not node.left and not node.right:
            if node.val == sumVal:
                self.result.append(copy(templist))

        if node.left:
            self.findPath(node.left, templist, sumVal - node.val)
        if node.right:
            self.findPath(node.right, templist, sumVal - node.val)
        
        templist.pop()

# Method 2: define func findPath(node, templist, sumVal)
# Step 1: if node if leaf node and sumVal == node.val, result.append(templist + [node.val])
# Step 2: call findPath() in LST, with givenSum - node.val and templist + [node.val]
# Step 3: call findPath() in RST, with givenSum - node.val and templist + [node.val]

    def pathSum2(self, root, sumVal):
        self.paths = []

        def findPath(node, sumVal, templist):
            if not node.left and not node.right:
                if sumVal == node.val:
                    self.paths.append(templist + [node.val])
                return
            
            if node.left:
                findPath(node.left, sumVal - node.val, templist + [node.val])
            if node.right:
                findPath(node.right, sumVal - node.val, templist + [node.val])
        
        if root:
            findPath(root, sumVal, [])
            
        return self.paths


node = TreeNode(5)
l = TreeNode(4)
r = TreeNode(8)
ll = TreeNode(11)
lll = TreeNode(7)
llr = TreeNode(2)
rl = TreeNode(13)
rr = TreeNode(4)
rrl = TreeNode(5)
rrr = TreeNode(1)

node.left = l
node.right = r
l.left = ll
ll.left = lll
ll.right = llr
r.left = rl
r.right = rr
rr.left = rrl
rr.right = rrr

sol = Solution()
print(sol.pathSum2(node, 22))

