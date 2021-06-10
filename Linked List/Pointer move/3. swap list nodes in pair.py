# Given linked list, swap every two adjacent nodes
# 1 2 3 4 ::: 2 1 4 3

class Node:
    def __init__(self, data) -> None:
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def swapNodes(self, head):
        if head is None or head.next is None:
            return head

        temp = Node(-1)
        temp.next = head
        curr = temp

        while curr.next and curr.next.next:
            fptr = curr.next
            sptr = curr.next.next
            fptr.next = sptr.next
            curr.next = sptr
            curr.next.next = fptr

            curr = curr.next.next
        return temp.next

    def printll(self, head):
        ptr = head
        while ptr:
            print(ptr.data, end="-> ")
            ptr = ptr.next
        print()

llist = LinkedList()
n1 = Node(10)
n2 = Node(21)
n3 = Node(32)
n4 = Node(43)
n5 = Node(54)
n6 = Node(65)
n7 = Node(76)
n8 = Node(87)
n9 = Node(98)
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
no = llist.swapNodes(n1)
llist.printll(no)
