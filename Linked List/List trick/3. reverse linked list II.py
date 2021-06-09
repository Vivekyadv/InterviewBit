# given head of linked list, m and n integers
# reverse the linked list from m to n
# 
# Examnle = 1->2->3->4->5->     m = 2, n = 4
# output  = 1->4->3->2->5->

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  

class LinkedList:
    def __init__(self):
        self.head = None
    
    def reversesublist(self, head, m, n):
        before = Node(None)
        before.next = head
        temp = head
        for _ in range(m-1):
            before = before.next
            temp = temp.next
        firstToReverse = temp
        n_ = temp.next
        for _ in range(n-m):
            nn = n_.next
            n_.next = temp
            temp = n_
            n_ = nn
        firstToReverse.next = n_
        before.next = temp
        return head if m > 1 else before.next
    
    def reversesublist(self, head, m, n):
        if head.next is None:
            return head

        curr = head
        p = None
        count = 1
        while curr and count < m:
            p = curr
            curr = curr.next
            count += 1
        before = curr
        prev = None
        loop = (n-m)+1
        while curr and loop:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            loop -= 1
        before.next = next
        if p:
            p.next = prev
            return head
        else:
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
no = llist.reversesublist(n1,3, 6)

llist.printll(no)