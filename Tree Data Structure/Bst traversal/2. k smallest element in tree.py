# Given BST, write a func to find the kth smallest element in the tree
# Tree         4
#            /    \
#           2       6
#          / \     / \
#         1   3   5   7
# 3th smallest element = 3

# Method 1: using inorder traversal
# inorder traversal gives sorted list, then find kth element in sorted list

def kthsmallest(root, k):
    ans = []
    def inorder(root, ans):
        if root:
            inorder(root.left, ans)
            ans.append(root.val)
            inorder(root.right, ans)
        else: return
    
    inorder(root, ans)
    return ans[k-1]


# Method 2: idea is to mainitain the rank of each node.
# assume root is having 'lcount' nodes in its left sebtree.
# if k == lcount + 1 --> that mean kth value is root
# if k < lcount + 1  --> we'll continue our search in left subtree
# if k > lcount + 1  --> search in right subtree for k - (lcount+1) nodes because 
#       lcount + 1 nodes are already counted in left subtree. so we have to search for
#       remaining nodes k - (lcount + 1)

def count(root):
    if not root:
        return 0
    return 1 + count(root.left) + count(root.right)

def kthsmallest(root, k):
    lcount = count(root.left)
    if lcount + 1 == k:
        return root.val
    elif lcount + 1 > k:
        return kthsmallest(root.left, k)
    else:
        return kthsmallest(root.right, k - (lcount+1))

