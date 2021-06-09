# check wether given linked list is palindrome or not

# Method: use stack to check palindrome
# append each element of llist, then in a loop, pop element from stack
# and check it with element of llist
class Node:
    def __init__(self, data) -> None:
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def isPalindrome(self, head):
        stack = []
        ispali = True

        # iterate from head to end of llist and append node's value in stack
        ptr = head
        while ptr:
            stack.append(ptr.data)
            ptr = ptr.next
        
        # iterate again, pop element from stack and check it with node's value
        # if value == popped element --> move forward, else not palindrome
        ptr = head
        while ptr:
            val = stack.pop()
            if ptr.data != val:
                ispali = False
                break
            ptr = ptr.next
        
        return ispali

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
n5 = Node(3)
n6 = Node(2)
n7 = Node(1)
llist.head = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
llist.printll(n1)
print(llist.isPalindrome(n1))
# no = llist.removeduplicate(n1)
# llist.printll(no)