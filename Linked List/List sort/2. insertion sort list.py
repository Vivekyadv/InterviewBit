# sort a linked list using insertion sort

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def insert(self, prev, node):
        node.next = prev.next
        prev.next = node
    
    def insertionSort2(self, a):
        head = Node(-float('inf'))
        while a:
            prev = head 
            node = prev.next
            while node:
                if node.data > a.data:
                    break
                prev = node
                node = node.next
            self.insert(prev, Node(a.data))
            a = a.next
        return head.next

    def insertionSort(self, a):
        head = Node(-float('inf'))
        head.next = a

        prev = a
        node = prev.next

        while node:
            if prev.data <= node.data:
                prev = node
                node = node.next
            else:
                before = head
                after = head.next
                prev.next = node.next

                while after and after.data < node.data:
                    before = after
                    after = after.next

                before.next = node
                node.next = after
                node = prev.next
            
        return head.next

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
res = llist.insertionSort2(h)
llist.printll(res)