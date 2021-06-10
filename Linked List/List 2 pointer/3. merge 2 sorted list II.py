# Given two sorted list, merge then and return in sorted order

from typing import Counter


class Node:
    def __init__(self, data) -> None:
        self.data = data 
        self.next = None
    
class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def merge(self, head1, head2):
        ptr1 = head1
        ptr2 = head2
        result = Node(None)
        ptr_res = result

        while ptr1 and ptr2:
            if ptr1.data < ptr2.data:
                ptr_res.next = Node(ptr1.data)
                ptr1 = ptr1.next
            else:
                ptr_res.next = Node(ptr2.data)
                ptr2 = ptr2.next
            ptr_res = ptr_res.next

        if ptr1 and ptr2 is None:
            while ptr1:
                ptr_res.next = Node(ptr1.data)
                ptr1 = ptr1.next
                ptr_res = ptr_res.next
        if ptr1 is None and ptr2:
            while ptr2:
                ptr_res.next = Node(ptr2.data)
                ptr2 = ptr2.next
                ptr_res = ptr_res.next
        return result.next

    def printll(self, head):
        ptr = head
        while ptr:
            print(ptr.data, end="-> ")
            ptr = ptr.next
        print()


llist1 = LinkedList()
h = Node(2)
h2 = Node(3)
h3 = Node(4)
h.next = h2
h2.next = h3
llist1.head = h
llist1.printll(h)

llist2 = LinkedList()
h4 = Node(5)
h5 = Node(6)
h6 = Node(7)
h4.next = h5
h5.next = h6
llist2.head = h4
llist2.printll(h4)
sort = llist1.merge(h,h4)
llist1.printll(sort)
