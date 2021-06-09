# Given a linked list and a key value, partition it such that all nodes 
# less than key come before nodes greater than or equal to key.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    # def append(self, head, node):
    #     if head is None:
    #         head = node
    #     else:
    #         end = head
    #         while end.next:
    #             end = end.next
    #         end.next = node
    #     return head
    #
    # def partition2(self, A, key):
    #     _1st = _2nd = None
    #     headOf_1 = headOf_2 = None
    #     head = A
    #     while head:
    #         if head.data < key:
    #             _1st = self.append(headOf_1, Node(head.data))
    #             headOf_1 = _1st
    #         else:
    #             _2nd = self.append(headOf_2, Node(head.data))
    #             headOf_2 = _2nd
    #
    #         head = head.next
    #
    #     if headOf_1:
    #         last = headOf_1
    #         while last.next:
    #             last = last.next
    #         last.next = headOf_2
    #         return headOf_1
    #     else:
    #         return headOf_2

    def partition(self, A, key):
        head1 = Node(0)
        head2 = Node(0)
        node1, node2 = head1, head2
        while A:
            if A.data < key:
                node1.next = A
                node1 = A
            else:
                node2.next = A
                node2 = A
            A = A.next
        node1.next = head2.next
        node2.next = None
        return head1.next

    def partition2(self, A, key):
        _1st, _2nd , headOf_1 = None, None, None
        head = A
        while head:
            if head.data < key:
                if _1st is None:
                    _1st = head
                    headOf_1 = _1st
                else:
                    _1st.next = head
                    _1st = _1st.next
            else:
                if _2nd is None:
                    _2nd = head
                    headOf_2 = _2nd
                else:
                    _2nd.next = head
                    _2nd = _2nd.next

            head = head.next
        _2nd.next = None

        if headOf_1:
            _1st.next = headOf_2
            return headOf_1
        else:
            return headOf_2

    def printll(self,head):
        ptr = head
        while ptr:
            print(ptr.data, end="-> ")
            ptr = ptr.next
        print()
    
llist = LinkedList()
h = Node(1)
h2 = Node(2)
h3 = Node(5)
h4 = Node(3)
h5 = Node(4)
h6 = Node(6)
h.next = h2
h2.next = h3
h3.next = h4
h4.next = h5
h5.next = h6
llist.head = h
llist.printll(h)
res = llist.partition(h,4)
llist.printll(res)