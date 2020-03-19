import math
a = int(input())
b = 0
for x in range(1,int(math.sqrt(a))):
	if a%x==0:
		b = b + 1
b = 2*b
d = int(math.sqrt(a))
d = d * d
if d == a:
	b = b + 1
print(b)