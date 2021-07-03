# Given a Binary tree, return the level order traversal of its nodes values.
# reverse order: from left to right and from last level to first level
#             1
#          /    \
#         2      3
#        / \    /   
#       4   5  6  
#          / \ 
#         7   8

# result = [7, 8, 4, 5, 6, 2, 3, 1]

class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

# Logic: In level order we move from left to right. In this case, move from right to
# left and after the loop, reverse the result.
# Example: in above tree, move from right to left: res = [1, 3, 2, 6, 5, 4, 8, 7]
# Now reverse the result = [7, 8, 4, 5, 6, 2, 3, 1]

from collections import deque
class Solution:
    def solve(self, root):
        queue = [root]
        result = []
        while queue:
            node = queue.pop(0)
            result.append(node.val)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        result = result[::-1]
        return result

    # or we can direclty append node.val at the start (index 0) of result
    def solve(self, root):
        queue = deque()
        queue.append(root)
        result = deque()
        while queue:
            node = queue.popleft()
            result.appendleft(node.val)
            
            if node.right:
                queue.append(node.right)            
            if node.left:
                queue.append(node.left)
        return result


node = TreeNode(1)
l = TreeNode(2)
ll = TreeNode(4)
lr = TreeNode(5)
lrl = TreeNode(7)
lrr = TreeNode(8)
r = TreeNode(3)
rl = TreeNode(6)

node.left = l
node.right = r
l.left = ll
l.right = lr
lr.left = lrl
lr.right = lrr
r.left = rl

sol = Solution()
print(sol.solve(node))