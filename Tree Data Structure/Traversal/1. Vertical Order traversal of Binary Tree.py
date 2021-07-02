# Given a binary tree consisting of n nodes, return 2D array denoting the vertical
# order traversal of tree
#
#           1
#          / \
#         2   8
#        / \   \         expected result: [[3,6], [2,4], [1,5,7], [8,11], [9], [12]]
#       3   5   9        preorder result: [[3,6], [2,4], [1,7,5], [8,11], [9], [12]]
#        \     / \
#         4   11  12
#        / \          
#       6   7  
#
# In question it mentioned to use preorder in case there are 2 or more nodes in same
# vertical line. its typing mistake so, this will not give expected result

from collections import deque

class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

# Modified Method: using level order traversal with deque to store nodes in the 
# same vertical, if they belong to same vertical number.      
class Solution: 
    def verticalOrderTraversal(self, root):
        table = {}
        queue = deque()
        if root == None:
            return []
        
        queue.append((root, 0 ))

        while len(queue):
            node, pos = queue.pop()
            if pos in table:
                table[pos].append(node.val)
            else:
                table[pos] = [node.val]

            if node.left:
                queue.appendleft((node.left, pos-1))
            if node.right:
                queue.appendleft((node.right, pos+1))
        
        
        result = []
        for key in sorted(table.keys()):
            result.append(table[key])
            
        return result

# We can solve this without using deque, some modification in above code
# line 30: queue = []
# line 37: node, pos = queue.pop(0)
# line 44: queue.append((node.left, pos-1))
# line 46: queue.append((node.right, pos+1))

node = TreeNode(1)
l = TreeNode(2)
ll = TreeNode(3)
lr = TreeNode(5)
llr = TreeNode(4)
llrl = TreeNode(6)
llrr = TreeNode(7)
r = TreeNode(8)
rr = TreeNode(9)
rrl = TreeNode(11)
rrr = TreeNode(12)

node.left = l
node.right = r
l.left = ll
l.right = lr
ll.right = llr
llr.left = llrl
llr.right = llrr
r.right = rr
rr.left = rrl
rr.right = rrr

sol = Solution()
print(sol.verticalOrderTraversal(node))


# below code use preorder method, so will give error in case of multiple nodes in
# single vertical line
# def verticalOrderTraversal(self, root):
#     self.table = {}
#     pos = 0
#     if root:
#         self.vertical(root, pos)

#     result = []
#     for key in sorted(self.table.keys()):
#         result.append(self.table[key])

#     return result

# def vertical(self, root, pos):
#     if pos in self.table:
#         self.table[pos].append(root.val)
#     else:
#         self.table[pos] = [root.val]
    
#     if root.left:
#         self.vertical(root.left, pos-1)
#     if root.right:
#         self.vertical(root.right, pos+1)
