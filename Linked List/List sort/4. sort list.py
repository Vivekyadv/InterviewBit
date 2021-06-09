# Sort linked list in O(nlogn) using O(1) space
# 
# Method 1: store values of linked list in array, sort it and then 
# modify values of linked list according to sorted array

# Method 2: use merge sort to solve

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Method 1: using list 
    def sort(self, A):
        if A == None:
            return None
        elif A.next == None:
            return A
        
        head = A
        result = []
        while head:
            result.append(head.data)
            head = head.next
        
        result.sort()

    # create a new Linked List
        # head = Node(result[0])
        # ptr = head
        # for i in range(1, len(result)):
        #     ptr.next = Node(result[i])
        #     ptr = ptr.next
        # A = head
    
    # or modify original Linked List
        head = A
        for i in range(len(result)):
            head.data = result[i]
            head = head.next

        return A



    # Method 2: using merge sort
    def sortList(self, A):
        if not A or not A.next:
            return A
        first, second = self.divide(A)
        first = self.sortList(first)
        second = self.sortList(second)
        return self.merge(first, second)
        
    def divide(self, head):
        prev, nextt = head, head.next
        while nextt.next:
            prev = prev.next
            nextt = nextt.next
            if nextt.next:
                nextt = nextt.next
        second_part = prev.next
        prev.next = None
        return head, second_part    
    
    def merge(self, first, second):
        if not first:
            return second
        if not second:
            return first
        left, right = first, second
        if left.data <= right.data:
            cur, head = left, first
            left = left.next
        else:
            cur, head = right, second
            right = right.next
        while left and right:
            if left.data <= right.data:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
        if left:
            cur.next = left
        if right:
            cur.next = right
        return head
    
    def printll(self, head):
        ptr = head
        while ptr:
            print(ptr.data, end="-> ")
            ptr = ptr.next
        print()
                
llist = LinkedList()
h = Node(7)
h2 = Node(3)
h3 = Node(5)
h4 = Node(9)
h5 = Node(2)
h6 = Node(6)
h.next = h2
h2.next = h3
h3.next = h4
h4.next = h5
h5.next = h6
llist.head = h
llist.printll(h)
res = llist.sortList(h)     # or res = llist.sort(h)
llist.printll(res)