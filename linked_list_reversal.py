# reverse a singly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        current = self.head
        if self.head is None:
            self.head = Node(data)
            return
        else:
            while current.next:
                current = current.next
            newNode = Node(data)
            current.next = newNode

    def reverse(self):
        currentnode = self.head
        prev = None
        while currentnode:
            nxt = currentnode.next
            currentnode.next = prev
            prev = currentnode
            currentnode = nxt
        self.head = prev

    def printList(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.reverse()

    ll.printList()
