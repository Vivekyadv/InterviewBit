# given head of linked list, reverse every k nodes
# Example: 1->2->3->4->5->6->7->8->9-> and k = 3
#           1->2->3     ->4->5->6->     7->8->9-> 
# result:   3->2->1     ->6->5->4->     9->8->7-> 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def kReverse(self, head, k):
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
        
        # do this above process on rest of nodes in list
        if nexxt:
            head.next = self.kReverse(nexxt, k)
        
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
no = llist.kReverse(n1,2)
llist.printll(no)
