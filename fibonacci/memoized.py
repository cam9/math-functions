d = {0:0,1:1}
def f(n):
	if n in d:
		return d[n]
	else:
		d[n] = f(n-1)+f(n-2)
		return d[n]

import time 
n = input("Enter n:")
s = time.time()
nth = f(n)
s = time.time()-s
print nth
print (s, "seconds")

n = input("Enter n:")
s = time.time()
nth = f(n)
s = time.time()-s
print nth
print (s, "seconds")
