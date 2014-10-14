import fileinput

s = ["5",
	"1 0 2 5 8", 
	"2 3 4 7 9", 
	"3 5 7 8 9", 
	"1 2 5 4 2", 
	"3 3 5 2 1"]

s = ["4",
	"0 2 1 3",
	"2 1 0 4",
	"3 3 3 3",
	"5 5 2 1"]

s = ["10",
"24 27 33 61 30 68 12 64 91 22",
"87 5 63 67 41 35 31 93 0 47",
"98 29 90 66 42 26 44 73 37 65",
"45 25 86 85 18 23 79 2 8 80",
"51 28 77 62 59 58 11 75 40 21",
"39 76 43 4 13 54 38 83 95 82",
"48 19 70 9 15 3 20 36 96 97",
"50 60 94 84 49 72 74 52 53 57",
"99 46 88 32 34 55 92 1 16 17",
"71 7 69 6 14 89 10 81 78 56"]

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

def isOutOfRange(x, y, max_size):
	if x < 0 or x >= max_size or y < 0 or y >= max_size:
		return True
	else:
		return False

def get_top_node(node, max_size, node_map):
	x = node.x
	y = node.y + 1
	if isOutOfRange(x,y,max_size):
		return None
	else: 
		return node_map[x][y]

def get_bottom_node (node, max_size, node_map):
	x = node.x
	y = node.y - 1
	if isOutOfRange(x,y,max_size):
		return None
	else: 
		return node_map[x][y]

def get_left_node (node, max_size, node_map):
	x = node.x - 1
	y = node.y 
	if isOutOfRange(x,y,max_size):
		return None
	else: 
		return node_map[x][y]

def get_right_node(node, max_size, node_map):
	x = node.x + 1
	y = node.y 
	if isOutOfRange(x,y,max_size):
		return None
	else: 
		return node_map[x][y]
	
#finds the lowest neighbor
def adjacent_Lowest (node, max_size, node_map):
	adjacent_node_list = []
	top_node = get_top_node(node, max_size, node_map)
	if top_node is not None:
		adjacent_node_list.append(top_node)
	bot_node = get_bottom_node(node, max_size, node_map)
	if bot_node is not None:
		adjacent_node_list.append(bot_node)
	left_node = get_left_node(node, max_size, node_map)
	if left_node is not None:
		adjacent_node_list.append(left_node)
	right_node = get_right_node(node, max_size, node_map)
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

def modified_BFS (curr_node, color_id, node_traversal_path, node_map):
	#add node to the path
	node_traversal_path.append(curr_node)
	#color the node
	node_map[curr_node.x][curr_node.y].color_id = color_id
	#if there exists a node with lower elevation than x
	adj_node = adjacent_Lowest(curr_node,matrix_length, node_map)
	#if the adj lowest node is not itself && not colored
	if adj_node != curr_node and adj_node.color_id == 0:
		modified_BFS (adj_node, color_id, node_traversal_path, node_map)
	#if the adj lowest node is not itself && colored
	elif adj_node != curr_node and adj_node.color_id != 0:
		#color the prev nodes and this node as the existing basin color
		for node in node_traversal_path:
			node.color_id = adj_node.color_id
		return 0
	#else this is the sink, end of modified BFS
	else:
		#exit recursion
		return 0

#initializes nodes with unique coordinates and their elevation onto a node map with null color_id = 0
node_map = [[Node( i, j, elevation_map[i][j]) for j in range(matrix_length)] for i in range(matrix_length)]
#unique color ids to identify unique basins
current_color_id = 1
#sort nodes into a sorted list
unsorted_nodes = [ node for x_row in node_map for node in x_row]
#sorts nodes from highest to lowest, in n lg n time
sorted_nodes = sorted(unsorted_nodes, key = lambda node: node.elevation, reverse=True )

#print "sorted nodes here"
#print [str(node.elevation) + " " + str(node.x) + " " + str(node.y) + " " + str(node.color_id) for node in sorted_nodes]

#main function
for i in range (0, len(sorted_nodes)):
	#if sorted_nodes[i] is uncolored
	if sorted_nodes[i].color_id == 0:
		node_traversal_path = []
		modified_BFS (sorted_nodes[i], current_color_id, node_traversal_path, node_map)
		current_color_id += 1

	else:
		continue
#turn the node_map into a dictionary to count the basin sizes
#color id is the key, and value is the size
basin_id_map = {}

for row in node_map:
	for node in row:
		if basin_id_map.has_key(node.color_id):
			basin_id_map[node.color_id] += 1
		else:
			basin_id_map[node.color_id] = 1

basin_size_list = []
for key in basin_id_map:
	basin_size_list.append(basin_id_map[key])

basin_size_list = sorted(basin_size_list, key = lambda x: x, reverse = True)
print basin_size_list

for row in node_map:
	output = ""
	for node in row:
		output += str(node.color_id) + " "
	print output
#print [node.color_id for x_row in node_map for node in x_row]
