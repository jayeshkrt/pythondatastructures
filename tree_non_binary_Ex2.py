################## Non binary tree Exercise 2 ######################
# Jayesh Kumar Tiwari
# 13 June 2021
#####################################################

class TreeNode:
	def __init__(self,data):
		self.data = data
		self.parent = None
		self.children = []

	def get_level(self):
		p = self.parent
		level = 0
		while p is not None:
			level +=1
			p = p.parent
		return level

	def add_child(self, child):
		child.parent = self
		self.children.append(child)

	def print_tree(self, level):
		if self.get_level() <= level:
			spaces = " " * self.get_level() * 3
			prefix = spaces + "|__" if self.parent else ""
			print(prefix+self.data)
			if self.children:
				for child in self.children:
					child.print_tree(level)
		else:
			pass

def build_tree():
	root = TreeNode("Global")
	india = TreeNode("India")
	usa = TreeNode("USA")
	gujrat = TreeNode("Gujrat")
	karnataka = TreeNode("Karnataka")
	nj = TreeNode("New Jersey")
	cf = TreeNode("California")
	root.add_child(india)
	root.add_child(usa)
	india.add_child(gujrat)
	india.add_child(karnataka)
	usa.add_child(nj)
	usa.add_child(cf)
	gujrat.add_child(TreeNode("Ahmedabad"))
	gujrat.add_child(TreeNode("Baroda"))
	karnataka.add_child(TreeNode("Bangluru"))
	karnataka.add_child(TreeNode("Mysore"))
	nj.add_child(TreeNode("Princeton"))
	nj.add_child(TreeNode("Trenton"))
	cf.add_child(TreeNode("San Francisco"))
	cf.add_child(TreeNode("Mountain View"))
	cf.add_child(TreeNode("Palo Alto"))

	return root

if __name__ == '__main__':
	root = build_tree()
	print("Enter level to which you want to print:\n")
	root.print_tree(2)
