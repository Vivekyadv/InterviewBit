# Given a binary Linked List, which contains 0 and 1
# sort the list

# Method: count no of 0s and 1s in LL
# traverse the list and fill count0 nodes with 0 and count1 nodes with 1

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
    
    def append(self, new_data):
        new_node = Node(new_data)
        last = self.head

        # if LL is empty, point head to new_node
        if last is None:
            self.head = new_node
            return
        
        # else find last node and point to new_node
        while last.next:
            last = last.next
        last.next = new_node

    # def sortlist(self):
    #     count = [0, 0]
    #     ptr = self.head
    #     while ptr:
    #         count[ptr.data] += 1
    #         ptr = ptr.next
        
    #     i = 0
    #     ptr = self.head
    #     while ptr:
    #         if count[i] == 0:
    #             i += 1
    #         else:
    #             ptr.data = i
    #             count[i] -= 1
    #             ptr = ptr.next

    def sortlist(self):
        count0 = count1 = 0
        ptr = self.head
        while ptr:
            if ptr.data == 0:
                count0 += 1
            else:
                count1 += 1
            ptr = ptr.next
        
        ptr = self.head
        count = 0
        while ptr:
            if count < count0:
                ptr.data = 0
                count += 1
            else:
                ptr.data = 1
            ptr = ptr.next

    def sortlist2(self):
        if self.head is None or self.head.next is None:
            return 
        zeroD = Node(0)
        oneD = Node(0) 
        ptr0 = zeroD
        ptr1 = oneD

        curr = self.head
        while curr:
            if curr.data == 0:
                ptr0.next = curr
                ptr0 = ptr0.next
            else:
                ptr1.next = curr
                ptr1 = ptr1.next
            curr = curr.next
        
        ptr0.next = oneD.next
        ptr1.next = None
        self.head = zeroD.next

    def printll(self):
        cur_node = self.head

        if cur_node is None:
            print("Empty Linked List")
            return
        while cur_node:
            print(cur_node.data, end="-> ")
            cur_node = cur_node.next
        print()

llist = LinkedList()
llist = LinkedList()
llist.push(0)
llist.push(1)
llist.push(1)
llist.push(0)
llist.push(1)
llist.push(0)
llist.push(0)
llist.push(1)
llist.push(0)
llist.push(1)
llist.printll()
llist.sortlist2()
llist.printll()