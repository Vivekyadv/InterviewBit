# Given a linked list A , reverse the order of all nodes at even positions.
# Example: 1 2 3 4 5 6 7 8      :: rev = 1 8 3 6 5 4 7 2

# Method: store nodes of even position in a stack and the in update the
# values at even pos using stack.pop()
class Node:
    def __init__(self, data) -> None:
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def reverselist(self, head):
        evenlist = []
        ptr = head
        ptr = head.next
        while ptr and ptr.next and ptr.next.next:
            evenlist.append(ptr.data)
            ptr = ptr.next.next

        if ptr:
            evenlist.append(ptr.data)

        ptr = head
        ptr = head.next
        while ptr and ptr.next and ptr.next.next:
            ptr.data = evenlist.pop()
            ptr = ptr.next.next
        
        if ptr and evenlist:
            ptr.data = evenlist.pop()
        return head
    
    def printll(self,head):
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
no = llist.reverselist(n1)
llist.printll(no)


    