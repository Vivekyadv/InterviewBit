class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def lengthOfList(self, head):
        n = 0
        ptr = head
        while ptr:
            ptr = ptr.next
            n += 1
        return n
    
    def remove(self, head, n):
        length = self.lengthOfList(head)
        prev_pos = length - n 

        # if n is >= len(list), delete first node 
        if prev_pos <= 0:
            return head.next

        # if n == 0, we dont have to delete anything
        if prev_pos == length:
            return head

        # find previous node [(n+1)th node from end]
        i = 1
        ptr = head
        while ptr and i < prev_pos:
            ptr = ptr.next
            i += 1
        
        # delete the nth node from end
        nextt = ptr.next
        ptr.next = nextt.next
        nextt.next = None
        return head
        
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
llist.head = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
llist.printll(n1)
head = llist.remove(n1,2)
llist.printll(head)
