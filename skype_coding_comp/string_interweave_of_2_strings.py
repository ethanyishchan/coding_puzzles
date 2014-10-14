def interweave(a,b,c,i=0,j=0,k=0):
	if len(a) + len(b) != len(c):
		return False
	#check if c is an interweave of a and b
	if k == len(c) -1:
		return True

	flag_i = False
	flag_j = False
	if i < len(a) and a[i] == c[k]:
		flag_i = interweave(a,b,c,i+1,j,k+1)
	if j < len(b) and b[j] == c[k]:
		flag_j = interweave(a,b,c,i,j+1,k+1)
	
	return flag_i or flag_j

b = "ABCDDDDDDD"
a = "ABCDEF"
c = "ABCDDDABCDDDEFDD"
print interweave(a,b,c)
