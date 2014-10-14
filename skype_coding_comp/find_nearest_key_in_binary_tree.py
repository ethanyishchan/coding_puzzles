# For an array of integers, give an algorithm to determine if there are three elements that sum to zero. What are the time and space complexity? Generalize to the case where the sum of k elements is 0?


# given a key, find the node with the nearest key

class node:
	def __init__(self,v,l= None,r = None):
		self.value = v
		self.left = l
		self.right = r

def print_v (node):
	print node.value

def printTree_preorder(node):
	if node is None:
		return
	print_v(node)
	printTree_preorder(node.left)
	printTree_preorder(node.right)

def printTree_inorder(node):
	if node is None:
		return
	printTree_inorder(node.left)
	print_v(node)
	printTree_inorder(node.right)

def printTree_postorder(node):
	if node is None:
		return
	printTree_postorder(node.left)
	printTree_postorder(node.right)
	print_v(node)

def construct_dummy():
	root = node(10,node(5,node(6),node(7)),node(16,node(14),node(20)))
	#root = node("F",node("B",node("A"),node("D", node("C"),node("E"))),node("G",None,node("I",node("H"),None)))
	return root

def find_key(key, node):
	if node is None:
		return False

	if key == node.value:
		return True,node
	
	return find_key(key, node.left) \
			or find_key(key, node.right)

def insert_key(key,curr_node):

	if key > curr_node.value and curr_node.right is None:
		curr_node.right = node(key)
	if key < curr_node.value and curr_node.left is None:
		curr_node.left = node(key)
	if key > curr_node.value:
		insert_key(key, curr_node.right)
	if key < curr_node.value:
		insert_key(key, curr_node.left)

def BFS (curr_node, limit=4):
	queue = []
	queue.append((curr_node, 0))

	while len(queue):
		node,depth = queue.pop(0)

		if depth == limit:
			break
		print node.value
		if node.left is not None:
			queue.append((node.left,depth+1))
		if node.right is not None:
			queue.append((node.right,depth+1))

def DFS (curr_node):
	stack = []
	stack.append((curr_node, 0))

	while len(stack):
		node,depth = stack.pop()
		print node.value
		if node.right is not None:
			stack.append((node.right,depth+1))
		if node.left is not None:
			stack.append((node.left,depth+1))


root_node = construct_dummy()
print "preorder: "
printTree_preorder(root_node)
print "inorder: "
printTree_inorder(root_node)
print "postorder: "
printTree_postorder(root_node)

print find_key(40,root_node)

insert_key(15, root_node)
printTree_inorder(root_node)

print find_key(15,root_node)

BFS(root_node)

print "DFS now"
DFS(root_node)