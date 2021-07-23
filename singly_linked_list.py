# Singly Linked List
class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

class linkedlist:
  def __init__(self):
    self.head = None
  
  def listLength(self):
    counter = 0
    currentNode = self.head
    while currentNode is not None:
      counter += 1
      currentNode = currentNode.next
    return counter

  def add_to_end(self, newNode):
    if self.head is None:
      self.head = newNode
      return
    else:
      lastNode = self.head
      while True:
        if lastNode.next is None:
          lastNode.next = newNode
          break
        lastNode = lastnode.next
  
  def add_to_front(self, newNode):
    if self.head is None:
      self.head = newNode
      return
    else:
      temp = self.head
      self.head = newNode
      self.head.next = temp
      # del(temp)
      
  def add_at_position(self, position, newNode):
    if position <0 or position >= self.listLength():
      print("position not in range of linked list!")
      return
    elif position ==0:
      self.add_at_front(newNode)
    else:
      counter = 0
      currentNode = self.head
      while counter <= position-1:
        temp = currentNode
        currentNode = currentNode.next
        counter+=1
      temp.next = newNode
      temp = currentNode
      newNode.next = temp
      currentNode = newNode
      
  def printlist(self):
    currentNode = self.head
    while currentNode is not None:
      print(currentNode.data)
      currentNode = currentNode.next
      
  def delete_at_pos(self, position):
    if position==0:
      self.head = self.head.next
      return
    elif position<= self.listLength()-1:
      counter = 0
      currentNode = self.head
      while counter <=position+1:
        if counter == position-1:
          temp = currentNode
        if counter == position+1:
          temp.next = currentNode
          return
        currentNode = currentNode.next
        counter+=1
    else:
      print("input position out of list length")
      return


if __name__ == "__main__":
  node1 = Node("apple")
  node2 = Node("boy")
  node3 = Node("cat")
  node4 = Node("dog")
  ll = linkedlist()
  ll.add_to_front(node1)
  ll.add_to_end(node2)
  ll.add_to_front(node3)
  ll.add_at_position(2, node4)
  
  ll.delete_at_pos(4)
  
  ll.printlist()
