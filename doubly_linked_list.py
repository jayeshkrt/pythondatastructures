# doubly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class dll:
    def __init__(self):
        self.head = None

    def listlength(self):
        counter = 0
        currentnode = self.head
        while currentnode:
            currentnode = currentnode.next
            counter += 1
        return counter

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        elif self.head.next is None:
            newNode = Node(data)
            self.head.next = newNode
            newNode.prev = self.head
            
        
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        newNode = Node(data)
        current_node.next = newNode
        newNode.prev = current_node

    def prepend(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode

    def printList(self):
        current_node = self.head
        while current_node.next:
            print(current_node.data)
            current_node = current_node.next

    def delete(self, position):
        counter =0
        if position == 0:
            self.head.next = self.head
            self.head.prev = None
            return
        elif position <0 or position > self.listlength():
            print("position out of list length")
            return
        else:
            counter = 0
            currentnode = self.head
            while counter < position:
                if counter == position-1:
                    temp = currentnode
                currentnode = currentnode.next
                counter += 1
            temp.next = currentnode.next
            currentnode.prev = temp
            del(temp)

if __name__=="__main__":
    dll1 =dll()
    dll1.append(2)
    dll1.append(9)
    dll1.prepend(6)

    print("Before deletion: \n") 
    dll1.printList()
    dll1.delete(3)
    print("After deletion: ")
    dll1.printList()
