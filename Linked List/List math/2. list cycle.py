# Detect loop in a linked list, if there is loop, return its node
# else return None         ____
#                         |    |
# LList::           1->2->3->4->
class Node:
    def __init__(self, data) -> None:
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    # using set(), find if we visited a node twice
    # NOTE: we can use list() but finding element in list takes O(n)
    # time which makes the whole algo O(n^2). And set() takes O(1) 
    def detectCycle(self, head):
        visited = set()
        while head:
            if head.data in visited:
                return head.data
            else:
                visited.add(head.data)
                head = head.next
        return None

    # Method 2: using Floyd’s Cycle-Finding Algorithm 
    def detectCycle2(self, head):
        ptr1 = ptr2 = head
        res = 0
        while ptr1 and ptr2 and ptr2.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
            if ptr1 == ptr2:
                res = 1
                break
        
        if res == 0:
            return None
        
        ptr1 = head
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return ptr1

llist = LinkedList()
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
llist.head = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n3
cycle = llist.detectCycle(n1)
print(cycle)