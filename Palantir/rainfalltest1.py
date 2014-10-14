import numpy

import fileinput

line_array = []
for line in fileinput.input():
    line_array.append(line)

class Node:
	def __init__(self, x, y, elevation, color_id = 0):
		self.x = x
		self.y = y
		self.elevation = elevation



input it as a double array with a value

create a hashmap and dump all the coordinates in with their position

sort the nodes into a list starting from the top to bottom

#color id is the key, and value is the size
basin_id_map = {}
#unique color ids to identify unique basins
current_color_id = 1

#main function
for i in xrange (0, len(sorted_node_list)):
	x = sorted_node_list[i]
	#if x is uncolored
	if x.color_id == 0:
		modified_BFS (x, current_color_id)
		#increment the unique id
		basin_size_array.append((current_color_id,0))
		current_color_id += 1

#finds the lowest neighbor
def adjacent_lowest (x):
	adjacent_lowest = min_value( for x in list of positions N,S,E,W of x)
	#if x is already the lowest, return itself
	if x.value < adjacent_lowest:
		return x 
	else:
		return adjacent_lowest

def modified_BFS (x, color_id):
	#color the node
	x.color = color_id
	#increase count of the basin_id_map
	basin_id_map[color_id] += 1
	#if there exists a node with lower elevation than x
	adj_node = adjacent_lowest(x)
	if adj_node != x:
		modified_BFS (adj_node, color_id)

def isSink(x):
	adj_list = N S E W

	for adj in adj_list:
		if x.elevation > adj.elevation:
			return false
	return true
		
