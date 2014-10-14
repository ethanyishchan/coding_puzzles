def com_substring (x, y , i=0 , j=0, count = 0, accum = ""):
	if i >= len(x):
		return count,accum
	if j >= len(y):
		return count,accum

	# copy = [x for x in accum]
	# copy = ''.join(copy)

	if x[i] == y[j]:
		accum = accum + x[i]
		return com_substring(x,y,i+1,j+1, count+1, accum)

	left = com_substring(x,y,i+1,j,count, accum)
	right = com_substring(x,y,i,j+1,count, accum)
	output = ""
	if left[0] >= right[0]:
		output = left
	else:
		output = right
	return output
	#return max (com_substring(x,y,i+1,j,count, accum) , com_substring(x,y,i,j+1,count, accum))

x = "whellothere"
y = "whowareyoutee"
print com_substring(x,y)