# Implement an iterator over a BST. Your iterator will be initialized with the root node.
# The first call to next() will return the smallest number in BST. Calling next() again 
# will return the next smallest number in the BST, and so on.

# Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, 
# where h is the height of the tree.

from heapq import *

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        arr = []
        self.preorder(root, arr)
        self.heap = arr
        
    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if len(self.heap) > 0 :
            return True 
        else :
            return False

    # @return an integer, the next smallest number
    def next(self):
        return heappop(self.heap)
        
        
    def preorder(self, root, heap):
        if root :
            heappush(heap,root.val)
            self.preorder(root.left, heap)
            self.preorder(root.right, heap)
            
            