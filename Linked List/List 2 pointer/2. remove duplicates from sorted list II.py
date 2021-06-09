class Node:
    def __init__(self, data) -> None:
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def removeduplicate(self, temp):
        curr = temp
        head = prev = Node(None)
        head.next = curr

        while curr and curr.next:
            if curr.data == curr.next.data:
                while curr and curr.next and curr.data == curr.next.data:
                    curr = curr.next
                curr = curr.next
                prev.next = curr

            else:
                prev = prev.next
                curr = curr.next
        return head.next

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
no = llist.removeduplicate(n1)
llist.printll(no)