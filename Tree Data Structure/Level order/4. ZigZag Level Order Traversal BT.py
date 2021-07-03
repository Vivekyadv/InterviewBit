# Given a binary tree, return the zigzag level order traversal of its nodes' value
# from left to right, then right to left from next level.
#             1
#          /    \
#         2      3
#        / \    /   
#       4   5  6  
#          / \ 
#         7   8

# result = [[1], [3, 2], [4, 5, 6], [8, 7]]

class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

# starting from level 0, when level % 2 == 1: we'll reverse the nodes of that level
# we'll use two stack (result, level_nodes). we store nodes of each level in level_nodes
# and check if this level % 2 == 1: if it is then reverse the level_nodes 
# then add the level_nodes in  result. 

class Solution:
    def zigzagLevelOrder(self, root):
        queue = [(root, 0)]
        result = []
        while queue:
            tempQueue = []
            level_nodes = []
            while queue:
                node, level = queue.pop(0)
                level_nodes.append(node.val)

                if node.left:
                    tempQueue.append((node.left, level+1))
                if node.right:
                    tempQueue.append((node.right, level+1))
            
            if level % 2 == 1:
                level_nodes = level_nodes[::-1]
            queue = tempQueue
            result.append(level_nodes)
        return result


    # Recursive method
    def helper(self, root, level, res):
            if root is None:
                return
            if len(res) < level + 1:
                res.append([])
            if level % 2 == 1:
                res[level].insert(0,root.val)
            else:
                res[level].append(root.val)
            self.helper(root.left,level+1,res)
            self.helper(root.right,level+1,res)
            
    
    def zigzagLevelOrder(self, root):
        if root is None:
            return None
        res = []
        level = 0
        self.helper(root,level,res)
        return res
        




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
print(sol.zigzagLevelOrder(node))

