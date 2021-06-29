# Given preorder and inorder traversal of a tree, construct the binary tree.

# Preorder : [1, 2, 3], Inorder  : [2, 1, 3]
# BST =   1
#        / \
#       2   3




# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

def construct(Pre, In, Is, Ie, Ps, Pe):
    ''' Pre: preorder, In: inorder, 
        Is: inorder start index, Ie: inorder end index
        Ps: preorder start index, Pe: preorder end index
    '''
    if Is > Ie or Ps > Pe:
        return None

    rootdata = Pre[Ps]

    # find index of the root. Note: In.index(rootdata) gives TLE
    indx = -1
    for i in range(Is, Ie+1):
        if In[i] == rootdata:
            indx = i
            break    
    
    # length of subtree
    leng = indx - Is
    
    root = TreeNode(rootdata)
    root.left = construct(Pre, In, Is, indx-1, Ps+1, Ps+leng)
    root.right = construct(Pre, In, indx+1, Ie, Ps+leng+1, Pe)
    
    return root

def buildTree(Pre, In):
    return construct(Pre, In, 0, len(In)-1, 0, len(Pre)-1)




# Method 2: Similar approach with less lines of code
def buildTree(Pre, In):
    if not In:
        return None
    
    # find index of root
    indx = In.index(Pre[0])

    root = TreeNode(Pre[0])
    root.left = buildTree(Pre[1:indx+1], In[:indx])
    root.right = buildTree(Pre[indx+1:], In[indx+1:])

    return root

