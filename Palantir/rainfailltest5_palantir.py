# Enter your code here. Read input from STDIN. Print output to STDOUT

#high level approach
#construct a 2D map containing nodes() to store the values
#create a list and sort the nodes according to their elevation
#starting from the highest to lowest elevation, start the Search on the node
    #for each node, run a SEARCH and color the lowest neighbouring nodes that are less than it
        #if SEARCH hits a color not already colored and is not itself:
            #color it and SEARCH on the new node
        #else if SEARCH hits a color that is already colored:
            #recolor the nodes on that path back to that color of the new adj node
            #return
        #else:
            #return
#compile results from the top

import fileinput
import sys

#create a node class
class Node:
    def __init__(self, x, y, elevation, color_id = 0):
        self.x = x
        self.y = y
        self.elevation = elevation
        #each node will belong to a color_id that corresponds to a basin
        self.color_id = color_id
        
#data input        
line_array = []
for line in fileinput.input():
    line_array.append(line)
matrix_length = int(line_array[0])
elevation_map = []
for x in xrange(1,len(line_array)):
    elevation_map.append(line_array[x].split())

#initializes nodes with unique coordinates and their elevation onto a 2D array with null color = 0
node_map = [[Node(i,j, elevation_map[i][j]) for j in range(matrix_length)] for i in range(matrix_length)]
#unique color id to identify unique basins
current_color_id = 1
#get all the nodes into a list
unsorted_nodes = [ node for x_row in node_map for node in x_row]
#sort them from highest to smallest elevation, O(N Lg N) time where N is number of points
#use pythons inbuilt quiksort
sorted_nodes = sorted(unsorted_nodes, key = lambda node: node.elevation, reverse = True)
#print [node.elevation for node in sorted_nodes]

def isOutOfRange(x, y, max_size):
    '''
    checks if x and y range is out of bounds of the node_map
    '''
    if x < 0 or x >= max_size or y < 0 or y >= max_size:
        return True
    else:
        return False

def get_top_node(node, max_size, node_map):
    '''gets the top node'''
    x = node.x
    y = node.y + 1
    if isOutOfRange(x,y,max_size):
        return None
    else: 
        return node_map[x][y]

def get_bottom_node (node, max_size, node_map):
    '''gets the bottom node'''
    x = node.x
    y = node.y - 1
    if isOutOfRange(x,y,max_size):
        return None
    else: 
        return node_map[x][y]
    
def get_left_node (node, max_size, node_map):
    '''gets the left node'''
    x = node.x - 1
    y = node.y 
    if isOutOfRange(x,y,max_size):
        return None
    else: 
        return node_map[x][y]

def get_right_node(node, max_size, node_map):
    '''gets the right node'''
    x = node.x + 1
    y = node.y 
    if isOutOfRange(x,y,max_size):
        return None
    else: 
        return node_map[x][y]
    
def adjacent_Lowest(node, max_size, node_map):
    '''
    finds and returns the lowest neighbor (top,bot,left,right) , if itself is already the lowest, it will return itself
    '''
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
    if len(sort_by_elevation):
        adjacent_lowest = sort_by_elevation[0]
    else:
        #no adjacent nodes, means it is its only node
        return 0

	#if x is already the lowest, return itself
    if node.elevation < adjacent_lowest.elevation:
        return node 
    else:
        return adjacent_lowest

def search_And_Color(curr_node, color_id, node_traversal_path, node_map):
    '''
    This function will conduct recursive search starting from the current node 
    with the condition that the next node will have to be the lowest neighbour
    and color it accordingly.1
    
    curr_node : to start BFS from
    color_id : basin id
    node_traversal_path : remember the search path to be able to back color the map
    node_map : 2D array storing the positions and elevation
    '''
    
    #add node to the path
    node_traversal_path.append(node_map[curr_node.x][curr_node.y])
    #color the node
    node_map[curr_node.x][curr_node.y].color_id = color_id
	#if there exists a node with lower elevation than x
    adj_node = adjacent_Lowest(curr_node,matrix_length, node_map)
    if adj_node == 0:
        return -1
	#if the adj lowest node is not itself && not colored
    if adj_node != curr_node and adj_node.color_id == 0:
        search_And_Color (adj_node, color_id, node_traversal_path, node_map)
	#if the adj lowest node is not itself && colored
    elif adj_node != curr_node and adj_node.color_id != 0:
		#color the prev nodes and this node as the existing basin color
        for node in node_traversal_path:
            node_map[node.x][node.y].color_id = adj_node.color_id
        return 0
	#else this is the sink, end of modified BFS
    else:
		#exit recursion
        return 0
    
#main
for i in xrange (0, len(sorted_nodes)):
    #if the node is not already colored
    curr_node = sorted_nodes[i]
    if node_map[curr_node.x][curr_node.y].color_id == 0:
        node_traversal_path = []
        result = search_And_Color(node_map[curr_node.x][curr_node.y], current_color_id, node_traversal_path, node_map)
        if result == -1:
            print "1"
            sys.exit()
        current_color_id +=1
    else:
        continue

#turn the node_map into a dictionary to count the basin sizes, color id is key, value will be size of basin
basin_id_map = {}

for row in node_map:
    for node in row:
        if basin_id_map.has_key(node.color_id):
            basin_id_map[node.color_id] += 1
        else:
            basin_id_map[node.color_id] = 1
#dump values into a list
basin_size_list = []
for key in basin_id_map:
    basin_size_list.append(basin_id_map[key])
#sort from biggest to smallest
basin_size_list = sorted(basin_size_list, key = lambda x : x, reverse = True)

#this will print out the results
output_result = ""
for x in range(0,len(basin_size_list)):
    if x == len(basin_size_list) - 1:
        output_result += str(basin_size_list[x])
        break;
    output_result += str(basin_size_list[x]) + " "
print output_result
    
#this will print out map to check the basin partitions
'''
for row in node_map:
    output = ""
    for node in row:
        output += str(node.color_id) + " "
    print output
'''

#the results are really really similar, I am still figuring out the subtlty in the difference of the logic. I believe given just a bit more time I will be able to find it, please consider, thanks!
#it does work for the 4 basic test cases given above
