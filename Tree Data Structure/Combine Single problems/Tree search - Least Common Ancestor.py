# Find the lowest common ancestor in an unordered binary tree given two values in the tree.

#         3
#      /     \
#     5       1
#    / \     / \
#   6   2   0   8
#      / \
#     7   4

# the LCA of nodes 5 and 1 is 3. and LCA for nodes 5 and 4 is 5

# Logic: find the path from root -> node1 and path from root -> node2
# then compare both paths, the index at which both differ, index-1 is the result

# For node 6 and 4:
# path for 6 = [3, 5, 6] and path for 4 = [3, 5, 2, 4]. at index 2 both paths are diff
# so result is indx-1 i.e path[1] = 5

class Node:
	def __init__(self, x) -> None:
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def pathToNode(self, root, path, value):
		if not root:
			return False
		
		path.append(root.val)
		if root.val == value:
			return True

		if root.left and self.pathToNode(root.left, path, value) or \
			root.right and self.pathToNode(root.right, path, value):
			return True
		
		path.pop()
		return False

	def lca(self, root, node1, node2):
		path1 = []
		path2 = []

		# if both path exists then find lowest common ancestor
		if self.pathToNode(root, path1, node1) and self.pathToNode(root, path2, node2):
			i = 0
			while i < len(path1) and i < len(path2):
				if path1[i] != path2[i]:
					break
				i += 1
			return path1[i-1]
		else:
			return -1



root = Node(3)
root.left = Node(5)
root.right = Node(1)
root.left.left = Node(6)
root.left.right = Node(2)
root.left.right.left = Node(7)
root.left.right.right = Node(4)
root.right.left = Node(0)
root.right.right = Node(8)

sol = Solution()
print('5, 8:', sol.lca(root, 5, 8))
print('4, 6:', sol.lca(root, 4, 6))
print('7, 1:', sol.lca(root, 7, 1))
print('4, 5:', sol.lca(root, 4, 5))


# Editorial Solution
def lca(A, B, C):
	path1 = getPath(A, B)
	path2 = getPath(A, C)
	lca = -1
	for a, b in zip(path1, path2):
		if a is not b:
			break
		lca = a.val
	
	return lca

def getPath(root, val):
	if not root:
		return []
	if root.val == val:
		return [root]
	
	left = getPath(root.left, val)
	right = getPath(root.right, val)
	if right:
		return [root] + right
	if left:
		return [root] + left
	return []

 