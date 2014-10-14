content = []
with open("PracticeInput_anagram.txt") as f:
    content = f.readlines()
#print content


def get2words (s):
	s = s[1:-2]
	s = "".join(s)
	s = s.strip()
	s = s.split("\",\"")
	return s



def checkAnagram_help (dict1, dict2):
	    if len(dict1) != len(dict2):
	        print "Invalid Pattern"
	        return
	    
	    for key in dict1:
	        if dict2.has_key(key):
	            if dict2[key] != dict1[key]:
	                print "Invalid Pattern"
	                return
	        else:
	            print "Invalid Pattern"
	            return
	    print "Valid Pattern"
	    return

def checkAnagram( line_array):
	line_dictionary_array = [{},{}]
	for x in range (0,2):
	    for c in line_array[x]:
	        if line_dictionary_array[x].has_key(c) and c != "\n":
	            line_dictionary_array[x][c] += 1
	        elif c != "\n":
	            line_dictionary_array[x][c] = 1

    checkAnagram_help(line_dictionary_array[0], line_dictionary_array[1])


list_of_tuples = []
for line in content:
	list_of_tuples.append(get2words(line))

# for line in list_of_tuples:
# 	checkAnagram(line)
