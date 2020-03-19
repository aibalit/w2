import math
a = int(input())
b = int(input())
for x in range(a,b + 1):
	b = math.sqrt(x)
	c = int(b)
	if c*c == x:
		print(x)