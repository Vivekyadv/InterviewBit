# Given a Binary tree containing 0-9 integers. each root->leaf represent number
# example: 1->3->6  136
# find total sum of all root-to-leaf numbers % 1003
#           1
#        /    \
#       2      3               sum = 124 + 125 + 136 + 1378 + 1379
#      / \    / \
#     4   5  6   7
#               / \
#              8   9

class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

# Method 1: define a function findPath(root, templist) which takes node and list
# Step 1: append node.val in string format
# Step 2: if node is leaf node, update total sum += int(templist)
# Step 3: call findPath() in LST and then in RST
# Step 4: after traversing LST and RST, pop top element from templist (for backtracking)

class Solution:
    def sumNumbers(self, root):
        self.total = 0
        templist = []
        if root:
            self.findPath(root, templist)
        return self.total%1003
    
    def findPath(self, root, templist):
        templist.append(str(root.val))
        
        # if node is leaf nide
        if not root.left and not root.right:
            self.total += int(''.join(templist))
        
        # if left node exist, call findPath() for left subtree
        if root.left:
            self.findPath(root.left, templist)
        
        # if right node exist, call findPath() for right subtree
        if root.right:
            self.findPath(root.right, templist)
            
        # after converting root->leaf into number, delete last element of templist
        templist.pop()

# Method 2: define func findPath(root, value), which take node and from root value till node
# Step 1: if node is None, return 0
# Step 2: calculate value = value*10 + node.val
# Step 3: if node is leaf node, return the value
# Step 4: call findPath in LST and RST --> these func will return values from LST and RST
# Step 5: return the sum of values returned by LST and RST

    def sumNumbers(self, root):
    
        def findpath(root,value):
            if root is None:
                return 0
            value = (value*10+root.val)

            if root.left is None and root.right is None:
                return value

            left = findpath(root.left,value)
            right = findpath(root.right,value)
            return (left + right)
    
        return findpath(root,0)%1003

node = TreeNode(1)
l = TreeNode(2)
ll = TreeNode(4)
lr = TreeNode(5)
r = TreeNode(3)
rl = TreeNode(6)
rr = TreeNode(7)
rrl = TreeNode(8)
rrr = TreeNode(9)

node.left = l
node.right = r
l.left = ll
l.right = lr
r.left = rl
r.right = rr
rr.left = rrl
rr.right = rrr

sol = Solution()
print(sol.sumNumbers(node))

