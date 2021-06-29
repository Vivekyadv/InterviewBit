# Given a BST and integer k. find whether there exits two nodes whose sum = k
# Note: Your solution should run in linear time and not take memory more than 
# O(height of T).

# Method 1: using inorder traversal, create array in sorted form. Then using hashmap
# find if there exist two numbers whose sum = k

def t2sum(root, k):
    arr = []
    def inorder(root, arr):
        if root:
            inorder(root.left, arr)
            arr.append(root.val)
            inorder(root.right, arr)
        else: return
    
    inorder(root, arr)
    table = set()
    for val in arr:
        if k - val in table:
            return 1
        else:
            table.add(val)
    return 0


# Similar to above method:: Instead of array, we store val directly in hashtable
def t2Sum(self, root, k):
    table = set()
    def findpair(root, k, table):
        if root is None:
            return 0
        # search in left
        if findpair(root.left, k, table):
            return 1
        # root
        if table and k-root.val in table:
            return 1
        else:
            table.add(root.val)
        # search in right
        return findpair(root.right, k, table)
    
    if findpair(root, k, table):
        return 1
    else:
        return 0
# Time and space complexity: O(n)
# We need to optimise space complexity


# Will do this method later...
# def nextInorder(leftStack):
#     top = leftStack[-1]
#     while top.left is not None:
#         leftStack.append(top.left)


# def nextRevInorder(rightStack):
#     pass

# def solve(root, target):
#     leftStack = [root]
#     rightStack = [root]

#     leftNode = nextInorder(leftStack)
#     rightNode = nextRevInorder(rightStack)

#     while leftNode.val < rightNode.val:
#         if leftNode.val + rightNode.val == target:
#             return 1
#         elif leftNode.val + rightNode.val < target:
#             leftNode = nextInorder(leftStack)
#         else:
#             rightNode = nextRevInorder(rightStack)

