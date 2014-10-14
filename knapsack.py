sizes = [1,2,3,4,5]
points = [2,1,4,1,40]

size_limit = 10

#maximize points given size size_limit

def knapsack(sizes, points, limit, index = 0, curr_size=0, sack = [],score = 0):
	if index >= len(sizes):
		return score, sack
	#either include it inside or not.
	print sizes, points, "lim:", limit, "i:", index, "size:", curr_size, "---", sack
	old_size = curr_size
	curr_size += sizes[index]
	if curr_size > limit:
		return score, sack

	old_sack = [x for x in sack]
	sack.append(points[index])
	sack = [x for x in sack]

	include = knapsack(sizes,points,limit,index+1, curr_size, sack, score + points[index])
	exclude = knapsack(sizes,points,limit,index+1, old_size, old_sack, score)

	if include[0] > exclude[0]:
		return include
	else:
		return exclude

print knapsack(sizes,points,size_limit)