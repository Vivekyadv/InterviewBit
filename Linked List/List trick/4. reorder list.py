
class Node:
    def __init__(self, data) -> None:
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def reorder(self, head):
        arr = []
        tmp = head
        while tmp:
            arr.append(tmp.data)
            tmp = tmp.next
        tmp = head
        i = 0
        n = len(arr)
        while i < (n//2)+1 and tmp:
            tmp.data = arr[i]
            tmp = tmp.next
            if (n-i-1) != i:
                tmp.data = arr[n-i-1]
                tmp = tmp.next
            i += 1
        return head

    def printll(self, head):
        ptr = head
        while ptr:
            print(ptr.data, end="-> ")
            ptr = ptr.next
        print()

llist = LinkedList()
n1 = Node(10)
n2 = Node(21)
n3 = Node(32)
n4 = Node(43)
n5 = Node(54)
n6 = Node(65)
n7 = Node(76)
n8 = Node(87)
n9 = Node(98)
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
no = llist.reorder(n1)
llist.printll(no)
