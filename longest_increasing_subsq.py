#1 ---> brute force, n * 2^n

#2 ---> n^2 solution
def longest_subs(s, index=0, c = None, memo = {}):

	if index == len(s):
		return 0

	#dont include it
	m = longest_subs(s, index+1 , c)

	#include it, and find the max
	if s[index] > c:
		m =  max(1 + longest_subs(s,index+1,s[index]), m)

	#return result
	memo[str(index) + " " + str(c)] = m
	return memo[str(index) + " " + str(c)] 

s = [1,20,140,10401,104014,999939,13,10,9999999,2,3,10,5,6,7]
print longest_subs (s)


#3 ----> n solution

def longest_subs_n(s,index):
	if index == 0: 
		return 0
	m = 1
	for i in range (index):
		if s[i] < s[index-1]:
			m = max(m, 1+ longest_subs_n (s, i))

	return m


print "n solution"

print longest_subs_n (s, len(s))

