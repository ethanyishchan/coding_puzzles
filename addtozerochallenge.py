def sumToZero (num_list, k = 3,  accum = 0):
	print "k ", str(k)
	print "accum: ", str(accum)
	# if k == 0 and accum != 0:
	# 	#print "there is such a combination!"
	# 	return false
		#return True 
	for x in range (0, len(num_list)):
		number = num_list[x]
		trimmed_list = num_list [::x] + num_list [x::]
		#del trimmed_list[x]
		print trimmed_list
		sumToZero (trimmed_list, k-1, accum + number)
	

test_array_1 = [1,2,0,4,5,6,7,1,-2,3,-4,-10]

print test_array_1
print len(test_array_1)
test_array_2 = [-1,2,2,2,2,3,4,5,6]


print "array 1: ", str(sumToZero(test_array_1))
#print "array 2: ", str(sumToZero(test_array_2, 3, 0))