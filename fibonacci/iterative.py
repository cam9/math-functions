def f(n):
	prev = 0
	cur = 1
	fib = 0;
	for i in range(0, n):
		fib=cur+prev
		prev = cur
		cur = fib
	return fib

import time 
n = input("Enter n:")
s = time.time()
nth = f(n)
s = time.time()-s
print nth
print (s, "seconds")
