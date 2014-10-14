s = raw_input("Please enter a string to compress something: ")
print "you entered: ", s

def compress (s):
	print "Compressing: "
	if not s:
		return "NULL INPUT"
	if not len(s):
		return "EMPTY STRING"

	compressed_output = ""
	last_letter = s[0]
	last_letter_count = 0

	for x in range(0, len(s)):
		if s[x] == last_letter:
			last_letter_count += 1
			if x == len(s) -1:
				compressed_output += last_letter + str(last_letter_count)

		else:
			compressed_output += last_letter + str(last_letter_count)
			last_letter_count = 1
			last_letter = s[x]

	if len(s) < len(compressed_output):
		return s
	else:
		return compressed_output

print compress (s)

