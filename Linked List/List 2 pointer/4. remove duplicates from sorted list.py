class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def deleteNode(self, head):
        ptr = head
        if ptr is None:
            return
        while ptr.next:
            nextt = ptr.next
            if ptr.data == nextt.data:
                ptr.next = nextt.next
                nextt.next = None
            else:
                ptr = ptr.next
        return head
    
    def printll(self, head):
        ptr = head
        while ptr:
            print(ptr.data, end="-> ")
            ptr = ptr.next
        print()

    
llist = LinkedList()
n1 = Node(1)
n2 = Node(1)
n3 = Node(2)
n4 = Node(3)
n5 = Node(5)
n6 = Node(6)
n7 = Node(6)
llist.head = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
llist.printll(n1)
no = llist.deleteNode(n1)
llist.printll(no)



        

