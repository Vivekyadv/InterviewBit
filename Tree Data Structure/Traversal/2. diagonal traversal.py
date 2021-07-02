# Given Binary Tree, return all diagonal elements in a binary trree to same line
# consider line of slope -1 passing between nodes. use preorder traversal

#           1
#          / \
#         2   8
#        / \   \         diagonals: [[1, 8, 9, 12], [2, 5, 11], [3, 4, 7], [6]]
#       3   5   9        return: [1, 8, 9, 12, 2, 5, 11, 3, 4, 7, 6]
#        \     / \
#         4   11  12
#        / \          
#       6   7 

# Logic: in above tree, diagonals are 4, starting from 0,1,2,3
# when we move left of node, diagonal decrease by 1
# when we move right of node, diagonal remain unchanged
# nodes having same diagonals are stored together

class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    def solve(self, root):
        table = {}
        result = []
        if not root:
            return result
        self.preorder(root, 0, table)
        
        for key in sorted(table.keys()):
            for i in table[key]:
                result.append(i)
        return result
        
    def preorder(self, root, pos, table ):
        if not root:
            return
        
        if pos in table:
            table[pos].append(root.val)
        else:
            table[pos] = [root.val]
        
        self.preorder(root.left, pos+1, table)
        self.preorder(root.right, pos, table)
   

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
print(sol.solve(node))


# def solve(self, root):
#     result = []
#     node = root
#     queue = deque()
#     while node:
#         result.append(node.val)
#         if node.left:
#             queue.appendleft(node.left)
#         if node.right:
#             node = node.right
#         else:   
#             if len(queue) >= 1:
#                 node = queue.pop()
#             else:
#                 node = None
#     return result