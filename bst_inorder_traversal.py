################## Binary Search Tree #####################
# In order traversal building (as a list)
# no duplicate elemnents
# searching the tree O(logn) complexity
# Jayesh Kumar Tiwari
# 13 June 2021
#######################################################

class BSTnode:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	def add_child(self, data):
		if data == self.data:
			return	# node already exists

		if data < self.data:
			if self.left:
				self.left.add_child(data)
			else:
				self.left = BSTnode(data)

		else:
			if self.right:
				self.right.add_child(data)
			else:
				self.right = BSTnode(data)

	def search(self, val):
		if self.data == val:
			return

		if val < self.data:
			if self.left:
				return self.left.search(val)
			else:
				return False

		if val > self.data:
			if self.right:
				return self.right.search(val)
			else:
				return False

	def in_order_traversal(self):
		elements=[]
		if self.left:
			elements += self.left.in_order_traversal()

		elements.append(self.data)

		if self.right:
			elements += self.right.in_order_traversal()

		return elements

def build_tree(elements):
	print("input elements: ", elements)
	root = BSTnode(elements[0])

	for i in range(1,len(elements)):
		root.add_child(elements[i])

	return root

if __name__ == '__main__':
	fruits = ["apple","banana","pineapple","raspberry","guava","grapes","watermelon","kharbuja","grapes","tomato"]
	ft = build_tree(fruits)

	print("Is apple in the list? ",ft.search("apple"))
	print("Is kakadi in the list? ",ft.search("kakadi"))

	print("Sorted list is:\n")
	print(ft.in_order_traversal())
