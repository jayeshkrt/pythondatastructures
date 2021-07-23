################ Tree implementation #############
# Jayesh Kumar Tiwari
# 12 June 2021
# inspired from https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/7_Tree/7_tree.py 
####################################################

class TreeNode:
	def __init__(self, data):
		self.data = data
		self.children = []
		self.parent = None

	def get_level(self):
		level = 0
		p = self.parent
		while p:
			level += 1
			p = p.parent

		return level

	def print_tree(self):
		spaces = " " * self.get_level() * 3
		prefix = spaces + "|__" if self.parent else ""
		print(prefix + self.data)
		if self.children:
			for child in self.children:
				child.print_tree()

	def add_child(self, child):
		child.parent = self
		self.children.append(child)

def build_product_tree():
	root = TreeNode("Harry Potter")

	part1 = TreeNode("Philosopher's Stone")
	part1.add_child(TreeNode("Chess Match"))
	part1.add_child(TreeNode("Stone"))
	part1.add_child(TreeNode("Paltform 9 3/4"))

	part2 = TreeNode("Chamber of Sectrets")
	part2.add_child(TreeNode("Professor Lockhart"))
	part2.add_child(TreeNode("Tom Marvolo Riddle"))
	part2.add_child(TreeNode("Parsel Tongue"))

	part3 = TreeNode("Prisoner of Azkaban")
	part3.add_child(TreeNode("Serius Black"))
	part3.add_child(TreeNode("Peter Pettigrew"))

	root.add_child(part1)
	root.add_child(part2)
	root.add_child(part3)

	root.print_tree()

if __name__ == '__main__':
	build_product_tree()
