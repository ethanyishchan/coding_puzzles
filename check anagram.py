# Enter your code here. Read input from STDIN. Print output to STDOUT

import fileinput

line_array = []
for line in fileinput.input():
    line_array.append(line)
    
def checkAnagram (dict1, dict2):
    if len(dict1) != len(dict2):
        print "Not anagrams!"
        return
    
    for key in dict1:
        if dict2.has_key(key):
            if dict2[key] != dict1[key]:
                print "Not anagrams!"
                return
        else:
            print "Not anagrams!"
            return
    print "Anagrams!"
    return

line_dictionary_array = [{},{}]
for x in range (0,2):
    for c in line_array[x]:
        if line_dictionary_array[x].has_key(c) and c != "\n":
            line_dictionary_array[x][c] += 1
        elif c != "\n":
            line_dictionary_array[x][c] = 1
checkAnagram (line_dictionary_array[0], line_dictionary_array[1])
    
    