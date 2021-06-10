# Given linked list and a k value, rotate it by counter 
# clockwise by k nodes

class Node:
    def __init__(self, data) -> None:
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def rotate(self, head, k):
        curr = head
        last = None
        list_len = 0

        while curr:
            last = curr
            curr = curr.next
            list_len += 1

        k = k % list_len
        if k == 0:
            return head

        curr = head     

        for i in range(list_len - k-1):
            curr = curr.next

        new_head = curr.next
        curr.next = None
        last.next = head
        return new_head
 
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
no = llist.rotate(n1, 3)
llist.printll(no)
