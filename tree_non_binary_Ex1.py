############## Tree Non-Binary Exercise 1 #############
# Jayesh Kumar Tiwari
# 12 June 2021
#########################################################

class TreeNode:
	def __init__(self, designation, name):
		self.parent = None
		self.name = name
		self.designation = designation
		self.children = []

	def get_level(self):
		level = 0
		p = self.parent
		while p:
			level +=1
			p = p.parent
		return level

	def add_child(self, child):
		child.parent = self
		self.children.append(child)

	def print_tree(self, condition):
		# spaces = " "*self.get_level()*3
		# prefix = spaces + "|__" if self.parent else ""
		# print(prefix+self.name)
		# if self.children:
		# 	for child in self.children:
		# 		child.print_tree()
		if condition == "name":
			spaces = " " * self.get_level() * 3
			prefix = spaces+"|__" if self.parent else ""
			print(prefix+self.name)
			if self.children:
				for child in self.children:
					child.print_tree(condition)
		
		elif condition == "designation":
			spaces = " " * self.get_level() * 3
			prefix = spaces+"|__" if self.parent else ""
			print(prefix+self.designation)
			if self.children:
				for child in self.children:
					child.print_tree(condition)

		elif condition == "both":
			spaces = " " * self.get_level() * 3
			prefix = spaces + "|__" if self.parent else ""
			print(prefix + self.name+" ("+self.designation+")")
			if self.children:
				for child in self.children:
					child.print_tree(condition)

def build_management_tree():
	root = TreeNode("CEO","Nilupul")

	cto = TreeNode("CTO","Chinmay")
	ih = TreeNode("Infrastructure Head", "Vishwa")
	cto.add_child(ih)
	ih.add_child(TreeNode("Cloud Manager","Dhaval"))
	ih.add_child(TreeNode("App Manager","Abhijit"))
	cto.add_child(TreeNode("Application Head", "Aamir"))

	hr = TreeNode("HR Head", "Gels")
	hr.add_child(TreeNode("Recruitment Manager","Peter"))
	hr.add_child(TreeNode("Policy Manager","Waqas"))

	root.add_child(cto)
	root.add_child(hr)

	return root

if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree("name") # prints only name hierarchy
    root_node.print_tree("designation") # prints only designation hierarchy
    root_node.print_tree("both") # prints both (name and designation) hierarchy
	
