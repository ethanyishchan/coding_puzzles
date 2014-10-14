import fileinput

s = ["5",
	"1 0 2 5 8", 
	"2 3 4 7 9", 
	"3 5 7 8 9", 
	"1 2 5 4 2", 
	"3 3 5 2 1"]

class Node:
	def __init__(self, x, y, elevation, color_id = 0):
		self.x = x
		self.y = y
		self.elevation = elevation
		self.color_id = color_id

line_array = []
#for line in fileinput.input():
for line in s:
    line_array.append(line)
matrix_length = int(line_array[0])
elevation_map = []
for x in xrange(1, len(line_array)):
	elevation_map.append(line_array[x].split())

#->>>> check inputs
class ptr:
    def __init__(self, obj): self.obj = obj
    def get(self):    return self.obj
    def set(self, obj):      self.obj = obj

def isOutOfRange(x, y, max_size):
	if x < 0 or x >= max_size or y < 0 or y >= max_size:
		return True
	else:
		return False

def get_top_node(node, max_size):
	x = node.x
	y = node.y + 1
	if isOutOfRange(x,y,max_size):
		return None
	else: 
		return node_map[x][y]

def get_bottom_node (node, max_size):
	x = node.x
	y = node.y - 1
	if isOutOfRange(x,y,max_size):
		return None
	else: 
		return node_map[x][y]

def get_left_node (node, max_size):
	x = node.x - 1
	y = node.y 
	if isOutOfRange(x,y,max_size):
		return None
	else: 
		return node_map[x][y]

def get_right_node(node, max_size):
	x = node.x + 1
	y = node.y 
	if isOutOfRange(x,y,max_size):
		return None
	else: 
		return node_map[x][y]
	
#finds the lowest neighbor
def adjacent_lowest (node, max_size):
	adjacent_node_list = []
	top_node = get_top_node(node, max_size)
	if top_node is not None:
		adjacent_node_list.append(top_node)
	bot_node = get_bottom_node(node, max_size)
	if bot_node is not None:
		adjacent_node_list.append(bot_node)
	left_node = get_left_node(node, max_size)
	if left_node is not None:
		adjacent_node_list.append(left_node)
	right_node = get_right_node(node, max_size)
	if right_node is not None:
		adjacent_node_list.append(right_node)

	#sort nodes from smallest to highest elevation
	sort_by_elevation = sorted(adjacent_node_list, key = lambda node: node.elevation, reverse = False)
	adjacent_lowest = sort_by_elevation[0]

	#if x is already the lowest, return itself
	if node.elevation < adjacent_lowest.elevation:
		return node 
	else:
		return adjacent_lowest

def modified_BFS (x, color_id, node_traversal_path):
	#add node to the path
	node_traversal_path.append(x)
	#color the node
	x.color = color_id
	print "colored it: ", str(x.color)
	#if there exists a node with lower elevation than x
	adj_node = adjacent_lowest(x,matrix_length)
	#if the adj lowest node is not itself && not colored
	print "adj node color id is : ", str(adj_node.color_id)
	if adj_node != x and adj_node.color_id == 0:
		modified_BFS (adj_node, color_id, node_traversal_path)
	#if the adj lowest node is not itself && colored
	elif adj_node != x and adj_node.color_id != 0:
		print "hello"
		#color the prev nodes and this node as the existing basin color
		for node in node_traversal_path:
			node.color_id = adj_node.color_id
			print adj_node.color_id
			print node.color_id
		return 0
	#else this is the sink, end of modified BFS
	else:
		#do nothing
		return 0

#initializes nodes with unique coordinates and their elevation onto a node map with null color_id = 0
node_map = [[Node( i, j, elevation_map[i][j]) for j in range(matrix_length)] for i in range(matrix_length)]
#color id is the key, and value is the size
basin_id_map = {}
#unique color ids to identify unique basins
current_color_id = 1
#sort nodes into a sorted list
unsorted_nodes = [ node for x_row in node_map for node in x_row]
#sorts nodes from highest to lowest, in n lg n time
sorted_nodes = sorted(unsorted_nodes, key = lambda node: node.elevation, reverse=True )

print "sorted nodes here"
print [str(node.elevation) + " " + str(node.x) + " " + str(node.y) + " " + str(node.color_id) for node in sorted_nodes]

#main function
for i in range (0, len(sorted_nodes)):
	#if sorted_nodes[i] is uncolored
	if sorted_nodes[i].color_id == 0:
		node_traversal_path = []
		modified_BFS (sorted_nodes[i], current_color_id, node_traversal_path)
		current_color_id += 1

	else:
		continue

print [node.color_id for node in sorted_nodes]
print "map here: below: "
print [node.color_id for x_row in node_map for node in x_row]
