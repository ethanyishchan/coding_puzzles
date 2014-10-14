def reverse(s,i=0):
	if i == len(s)/2  :
		return s
	s = [x for x in s]
	s[i],s[len(s)-i-1] = s[len(s)-i-1],s[i]
	''.join(s)
	return reverse(s, i+1)

print reverse("abcdefg")