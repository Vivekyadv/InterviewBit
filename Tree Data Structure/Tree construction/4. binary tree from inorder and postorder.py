# Given inorder and postorder traversal of a tree, construct the binary tree.
# inorder = [5, 10, 15, 20, 25, 30, 35]
# postorder = [5, 15, 10, 25, 35, 30, 20]

#            20
#          /   \
#         10    30
#        / \    / \
#       5  15  25 35 


# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
    
def construct(In, post):
    if not In:
        return None
    
    rootdata = post[-1]
    indx = In.index(rootdata)

    root = TreeNode(rootdata)
    root.left = construct(In[:indx], post[:indx])
    root.right = construct(In[indx+1:], post[indx:-1])

    return root



# Editorial solution
def buildTree(A, B):
    post = B
    ino = A
    root = TreeNode(post.pop())
    stack = [root]
    while True:
        if ino[-1] == stack[-1].val:
            temp = stack.pop()
            ino.pop()
            if len(ino) == 0:
                break
            if stack:
                if ino[-1] == stack[-1].val:
                    continue
            temp.left = TreeNode(post.pop())
            stack.append(temp.left)
        else:
            temp = TreeNode(post.pop())
            stack[-1].right = temp
            stack.append(temp)
    return root