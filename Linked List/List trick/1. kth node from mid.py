# Given head of linked list, find the kth value from the middle towards 
# beginning of linked list. 
# mid = n/2 + 1

# Logic: find the length of linked list
# mid = n/2 + 1     and kth from mid to begin--> mid-k-1 from starting
# so target indx = mid-k-1

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def length(self, head):
        ptr = head
        count = 0
        while ptr:
            count += 1
            ptr = ptr.next
        return count

    def kthvalue(self, A, k):
        n = self.length(A)
        mid = n//2 + 1
        target = mid-k

        if target <= 0:
            return -1

        ptr = A
        indx = 1
        while ptr:
            if indx == target:
                return ptr.data
            indx += 1
            ptr = ptr.next

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
ans = llist.kthvalue(h, 2)
print(ans)