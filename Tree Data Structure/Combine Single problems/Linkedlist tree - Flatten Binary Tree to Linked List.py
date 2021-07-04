# Given a binary tree, flatten it to a linked list in-place.

#         1
#        / \
#       2   5
#      / \   \
#     3   4   6
# 
# LinkedList =  1-> 2-> 3-> 4-> 5-> 6
# Note that the left child of all nodes should be NULL in flatten tree.

# Method 1: this is preorder traversal. Store the values in preorder and then make a new
# tree of these values

class TreeNode:
	def __init__(self, x) -> None:
		self.val = x
		self.left = None
		self.right = None

class Solution:
    def preorder(self, root, ans):
        if not root:
            return
        ans.append(root.val)
        self.preorder(root.left, ans)
        self.preorder(root.right, ans)
        
        return ans
        
    def flatten(self, root):
        nodeValues = self.preorder(root, [])
        newTree = TreeNode(None)
        curr = newTree
        
        for value in nodeValues:
            node = TreeNode(value)
            curr.right = node
            curr = curr.right
        
        return newTree.right


    # Method 2: Editorial solution
    def flatten(self, root):
        if not root:
            return None
        right = self.flatten(root.right)
        left = self.flatten(root.left)

        if left:
            root.right = left
            root.left = None
            if root.right and right:
                node = root.right
                while node.right:
                    node = node.right
                node.right = right
        return root
