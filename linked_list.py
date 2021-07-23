# linked list implementation
# create a node class
# create a linked list class
# add nodes to the linked list

class node:
	def __init__(self,data):
		self.data = data
		self.next = None

class linkedlist:
	def __init__(self):
		self.head = None

	def add(self, newNode):
		# head=>john->None
		if self.head is None:
			self.head = newNode
		# head=>john->Bull->None
		else:
			lastNode = self.head
			while True:
				if lastNode.next is None:
					break
				lastNode = lastNode.next
			lastNode.next = newNode

	def listlength(self):
		counter = 0
		currentNode = self.head
		while True:
			counter +=1
			if currentNode.next is None:
				break
			currentNode = currentNode.next
		return counter

	def printlist(self):
		if self.head is None:
			print("List is empty")
			return
		currentNode = self.head
		while True:
			print(currentNode.data)
			currentNode = currentNode.next
			if currentNode is None:
				break

	def add_at_head(self, newNode):
		temp = self.head
		self.head = newNode
		newNode.next = temp
		del temp

	def add_at_position(self, position, newNode):
		if position >0 and position<=self.listlength():
			currentNode = self.head
			for i in range(position):
				if i == position-1:
					temp = currentNode
				currentNode = currentNode.next
			temp.next = newNode
			newNode.next = currentNode
		elif position==0:
			self.add_at_head(newNode)
		else:
			print("Invalid position, enter less than listlength")
			return

firstnode = node("john")
LinkedList = linkedlist()

# add first node to the linked list
LinkedList.add(firstnode)

secondnode = node("Bull")
# add second node
LinkedList.add(secondnode)

thirdnode = node("apple")
LinkedList.add(thirdnode)

# insert a new node at the head
LinkedList.add_at_head(node("wick"))

# insert at position 2
LinkedList.add_at_position(10, node("hoalal"))

LinkedList.printlist()