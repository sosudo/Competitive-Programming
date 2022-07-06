import math
n = int(input())
def dist(x1, x2, y1, y2):
	return (x2-x1)**2+(y2-y1)**2
x = list(map(int, input().split()))
y = list(map(int, input().split()))
m = dist(x[0], x[1], y[0], y[1])
for i in range(n):
	for j in range(i+1, n):
		m = max(m, dist(x[i], x[j], y[i], y[j]))
print(m)
