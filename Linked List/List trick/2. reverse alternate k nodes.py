# given head of linked list, reverse every alternate k nodes
# Example: 1->2->3->4->5->6->7->8->9-> and k = 3
#           1->2->3     ->4->5->6->     7->8->9-> 
# result:   3->2->1     ->4->5->6->     9->8->7-> 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def alternate(self, head, k):
        current = head
        nexxt = prev = None
        count = 0

        # reverse first k node
        while current and count < k:
            nexxt = current.next
            current.next = prev
            prev = current
            current = nexxt
            count += 1

        # head is at kth node, so change next of head to current
        if head:
            head.next = current

        # current at kth node, pass it without change
        count = 0
        while current and count < k-1:
            current = current.next
            count += 1 
        
        # do this above process on rest of nodes in list
        if current:
            current.next = self.alternate(current.next, k)
        
        return prev
    
    def printll(self, head):
        ptr = head
        while ptr:
            print(ptr.data, end="-> ")
            ptr = ptr.next
        print()

llist = LinkedList()
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n9 = Node(9)
llist.head = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8
n8.next = n9
llist.printll(n1)
no = llist.alternate(n1,3)
llist.printll(no)

