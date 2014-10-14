
class node:
	def __init__(self):
		self.count = 0
		self.left = None
		self.right = None

def countpaths(node, accum):
	node.count += accum
	if node.left is not None:
		countpaths (node.left, node.count)
	if node.right is not None:
		countpaths (node.right, node.count)


countpaths(root, 1)