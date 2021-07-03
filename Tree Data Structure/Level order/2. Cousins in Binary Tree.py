# Given Binary tree, and a node value. Find all cousins of given node

#            1
#          /    \
#         2       3
#        / \    /   \ 
#       4   5  6     7
#      / \    / \   / \
#     8   9  10 11 12  13

# Given node = 11
# Result = [8, 9, 12, 13]

class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None


# Note: during level order traversal, if parent.left is given node or parent.right is 
# given node then children of this parent must not be store in result

# loop untill we find the level previous to level of given node
# and simple level order traversal
class Solution:
    def solve(self, root, value):
        found = False
        queue = [root]
        
        while queue and not found:
            
            q_len = len(queue)
            for i in range(q_len):
                node = queue.pop(0)

                if (node.left and node.left.val == value) or \
                    (node.right and node.right.val == value):
                    found = True
                else:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            
        return [node.val for node in queue]


node = TreeNode(1)
l = TreeNode(2)
ll = TreeNode(4)
lr = TreeNode(5)
r = TreeNode(3)
rl = TreeNode(6)
rr = TreeNode(7)
rrl = TreeNode(12)
rrr = TreeNode(13)
rll = TreeNode(10)
rlr = TreeNode(11)
lll = TreeNode(8)
llr = TreeNode(9)

node.left = l
node.right = r
l.left = ll
l.right = lr
r.left = rl
r.right = rr
rr.left = rrl
rr.right = rrr
rl.left = rll
rl.right = rlr
ll.left = lll
ll.right = llr

sol = Solution()
print(sol.solve(node, 11))
