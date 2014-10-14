input = [2,1,4,6,7,8,3,9,10,5]

def partition (input, pivot_index, low , high):
	lessthan = []
	greaterthan = []
	for i in range (low, high):
		if input[i] > input[pivot_index]:
			greaterthan.append (input[i])
		elif input[pivot_index] > input[i]:
			lessthan.append (input[i])
	print lessthan
	print input[pivot_index]
	print greaterthan
	output = lessthan + [input[pivot_index]] + greaterthan
	return output


def quickWrap(input, k):

	def quickselect(input , low, high, k):
		pivot_index = input[0]
		partitioned = partition(input, pivot_index, low , high) 
		print partitioned
		if pivot_index == k:
			print "highb"
			return input[pivot_index]
		if k > pivot_index + 1:
			quickselect (partitioned, pivot_index +1, high, k)
		elif k < pivot_index + 1 :
			quickselect (partitioned, low, pivot_index , k)
	print len(input)
	return quickselect(input, 0, len(input), k)
# print input
# print quickWrap(input, 6)


import random

def select(data, n):
    "Find the nth rank ordered element (the least value has rank 0)."
    data = list(data)
    if not 0 <= n < len(data):
        raise ValueError('not enough elements for the given rank')
    while True:
        pivot = random.choice(data)
        pcount = 0
        under, over = [], []
        uappend, oappend = under.append, over.append
        for elem in data:
            if elem < pivot:
                uappend(elem)
            elif elem > pivot:
                oappend(elem)
            else:
                pcount += 1
        if n < len(under):
            data = under
        elif n < len(under) + pcount:
            return pivot
        else:
            data = over
            n -= len(under) + pcount

print select(input, 8)