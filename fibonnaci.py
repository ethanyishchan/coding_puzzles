

def fib (n, memo ={}):
	if n <= 0:
		return None
	if n == 2:
		return 1
	if n == 1:
		return 1

	if n in memo:
		return memo[n]
	else:
		ans = fib(n-1) + fib(n-2)
		memo[n] = ans
		print ans
		return memo[n]

print fib(10)


# for i in range(10):
# 	print fib(i)