def match (a, b , i=0, j=0, accum=0, path = []):

	if i >= len(a) or j >= len(b):
		return accum,path

	if a[i] == b[j]:
		path.append(a[i])
		copy = [x for x in path]
		return match(a,b,i+1,j+1, accum+1, copy)

	copy = [x for x in path]
	option1 = match(a,b,i+1,j,accum,copy)
	option2 = match(a,b,i,j+1,accum,copy)

	if option1[0] > option2[0]:
		return option1
	else:
		return option2
	#return max (match(a,b,i+1,j,accum,path), match(a,b,i,j+1,accum,path))

a = "ghijasfdhjasdfhlk"
b = "abcdef"

print match (a,b,0,0,0,[])

