import time

num = 900
def factorial_memo (n,memo = {}):

	if n < 2:
		return 1
	if n not in memo:
		memo[n] = n * factorial_memo(n-1)
	return memo[n]

starttime = time.time()
print factorial_memo(num)
print "time: ", time.time() - starttime

print "slower below"
def factorial (n):

	if n == 0:
		return 1
	if n == 1:
		return 1

	return n * factorial(n-1)



vstarttime = time.time()
print factorial(num)
print "time: ", time.time() - vstarttime