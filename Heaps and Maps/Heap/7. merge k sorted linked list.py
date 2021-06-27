# Merge k sorted linked list and return it as one sorted list

# Example :
# 1 -> 10 -> 20
# 4 -> 11 -> 13
# 3 -> 8 -> 9

# will result in:::   1 -> 3 -> 4 -> 8 -> 9 -> 10 -> 11 -> 13 -> 20

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from heapq import *

def mergeKLists(self, A):
    head = tail = ListNode(-1)
    heap = [(node.val, node) for node in A if node]
    heapify(heap)

    while heap :
        val , node = heap[0]
        
        if node.next is None :
            heappop(heap)
        
        else :
            heapreplace(heap, (node.next.val, node.next))
        tail.next = node
        tail = tail.next
    return head.next 


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __lt__(self, other):
        return self.val < other.val

from heapq import *

def mergeKLists(A):
    head = tail = ListNode(-1)
    heap = []
    
    # insert all nodes of A in heap
    for i in range(len(A)):
        heappush(heap, A[i])
    
    # now pop from heap and sotre the values in tree
    while len(heap) > 1:
        min_ele = heappop(heap)
        tail.next = min_ele
        tail = tail.next
        if min_ele.next:
            heappush(heap, min_ele.next)
            min_ele.next = None
            
    tail.next = heap[0]
    
    return head.next
        



# store all node.val in array, sort the array and then create a tree using 
# those node.vals
def mergeKLists(A):
    arr = []
    for node in A:
        while node:
            arr.append(node.val)
            node = node.next

    arr.sort()
    tree = None
    cur = None

    for val in arr:
        if tree == None:
            tree = ListNode(val)
            cur = tree
        else:
            cur.next = ListNode(val)
            cur = cur.next
    return tree