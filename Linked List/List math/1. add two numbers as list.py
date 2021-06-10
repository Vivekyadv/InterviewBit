# Given two linked list represents as two numbers in reverse order
# add then and return resulted linked list
# Example:  (2 -> 4 -> 3) + (5 -> 6 -> 4)   result: 7 -> 0 -> 8
# 342 + 465 = 807

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def add_func(self, head1, head2):
        ptr1 = head1
        ptr2 = head2
        result = Node(None)
        ptr_res = result
        carry = 0
        while ptr1 or ptr2 or carry:
            if ptr1:
                val1 = ptr1.data
                ptr1 = ptr1.next
            else:
                val1 = 0

            if ptr2:
                val2 = ptr2.data
                ptr2 = ptr2.next
            else:
                val2 = 0

            add = val1 + val2 + carry
            summ = add % 10
            carry = add//10
            ptr_res.next = Node(summ)
            
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
h2 = Node(4)
h3 = Node(3)
# h.next = h2
# h2.next = h3
llist1.head = h
llist1.printll(h)

llist2 = LinkedList()
h4 = Node(5)
h5 = Node(6)
h6 = Node(4)
h4.next = h5
h5.next = h6
llist2.head = h4
llist2.printll(h4)
sumhead = llist1.add_func(h,h4)
llist1.printll(sumhead)
