# Given a binary tree root of integers. Return an array of integers representing the 
# right view of the Binary tree. Right view of a Binary Tree: is a set of nodes 
# visible when the tree is visited from Right side.

#             1
#          /    \
#         2      3
#        / \    /  
#       4   5  6  
#          / \ 
#         7   8

# Result = [1, 3, 6, 8]

class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

# Approach: while traversing for level order, store node.val with their level as index
# and then for left view -> take first element of each index (level)
#          for right view -> take last element of each index (level)

# for right view, we can traverse level order from right side, then we'll take first
# element of each level. In solution below, i use dict() to store right most value 
# with their indices (or level number)

class Solution:
    def solve(self, root):
        queue = [(root, 0)]
        indx = {}
        while queue:
            node, level = queue.pop(0)
            if level not in indx:
                indx[level] = node.val

            if node.right:
                queue.append((node.right, level+1))
            if node.left:
                queue.append((node.left, level+1))

        result = list(indx.values())
        return result


    # Without using hash table. use previous level to check if we already store the
    # value of that level. if prev_level != current level, then store val in result
    # and update prev_level = level in each iteration
    def solve(self, root):
        queue = [[root,0]]
        result = []
        prev_level = -1
        while queue:
            node, level = queue.pop(0)
            if prev_level != level:
                result.append(node.val)
                prev_level = level

            if node.right:
                queue.append([node.right,level+1])
            if node.left:
                queue.append([node.left,level+1])
            
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
# print(sol.levelorder(node))


# store nodes of same level together in a dict() or list
# def levelorder(self, root):
#         nodeAtLevel = {}
#         queue = [(root, 0)]
#         while queue:
#             node, level = queue.pop(0)
#             if level not in nodeAtLevel:
#                 nodeAtLevel[level] = [node.val]
#             else:
#                 nodeAtLevel[level].append(node.val)
            
#             if node.left:
#                 queue.append((node.left, level+1))
#             if node.right:
#                 queue.append((node.right, level+1))
        
#         return list(nodeAtLevel.values())

# returned value = [[1], [2,3], [4,5,6], [7,8]]

