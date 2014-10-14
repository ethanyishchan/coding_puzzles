import sys
#lines = sys.stdin.readlines()

with open("virus_people.txt") as f:
    content = f.readlines()

# lines =['5 10 3',
# 'AGGAAAAGAG',
# 'CGAGGCCAAC',
# 'GACAAAACCG',
# 'GCGACGCAGA',
# 'AACAGCGCAG',
# 'GCC']

lines = content

citizens, length_citizens, length_virus = map(int, lines[0].rstrip().split(' '))

lines = lines[1:]
citizens = lines[:len(lines) -1]
virus = lines[-1]

print "citizen array:" , citizens
print "Virus", virus
#match longest substring length
def match (p, v, i=0, j=0, count=0):
	if i >= len(p) or j >= len(v):
		return 0

	if p[i] == v[j]:
		return 1 + match(p, v, i+1, j+1)

	return max( match(p, v, i+1, j), match(p, v, i, j+1) )
		
tuple_array = []
for i in xrange (0, len(citizens)):
	x = match (citizens[i], virus, 0, 0, 0)
	tuple_array.append((i,x))

print sorted(tuple_array, key=lambda t : t[1])

sorted_array = sorted(tuple_array,  key = lambda x: x[0], reverse = False)

