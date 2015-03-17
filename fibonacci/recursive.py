def f(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return f(n-1)+f(n-2)

import time 
n = input("Enter n:")
s = time.time()
nth = f(n)
s = time.time()-s
print nth
print (s, "seconds")
