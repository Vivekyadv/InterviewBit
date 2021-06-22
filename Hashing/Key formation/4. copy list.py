# Given a LinkedList in which each node contains an aditional random pointer which
# points to any node in list or NULL. Return a deep copy of list.


class RandomListNode:
    def __init__(self, x):
        self.data = x
        self.next = None
        self.random = None

def copyRandomList(head):
    if head is None:
        return head
    
    # Add new nodes into the hashmap
    # with original nodes as keys and
    # new nodes as values.
    Map = dict()
    cur = head
    while cur != None:
        Map[cur] = RandomListNode(cur.data)
        cur = cur.next
    
    # Traverse the linked list and
    # add the pointers for values.
    cur = head
    while cur != None:
        temp1 = Map[cur]
        temp2 = Map.get(cur.next, None)
        temp1.next = temp2
        cur = cur.next
    
    # Add the random pointers in same
    # way of the original linked list.
    cur = head
    while cur != None:
        temp1 = Map[cur]
        temp2 = Map.get(cur.random, None)
        temp1.random = temp2
        cur = cur.next
    
    return Map[head]


from collections import defaultdict
def copyRandomList(self, head):

    d = defaultdict(lambda: RandomListNode(0))
    d[None] = None
    m = head
    
    while m :
        d[m].label = m.label
        d[m].next = d[m.next]
        d[m].random = d[m.random]
        m = m.next
        
    return d[head]