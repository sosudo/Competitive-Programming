import sys
sys.stdin = open('triangles.in', 'r')
sys.stdout = open('triangles.out', 'w')
n = int(input())
x = []
y = []
for i in range(n):
	z = [int(i) for i in input().split()]
	x.append(z[0])
	y.append(z[1])
_max = 0
def dist(a, b):
	return ((b[0]-a[0])**2+(b[1]-a[1])**2)**(1/2)
for i in range(n):
	for j in range(i+1, n):
		for k in range(i+2, n):
			if x[i] == x[j] or x[j] == x[k] or x[k] == x[i] and not(x[i] == x[j] and x[j] == x[k] and x[k] == x[i]):
				if y[i] == y[j] or y[j] == y[k] or y[k] == y[i] and not(y[i] == y[j] and y[j] == y[k] and y[k] == y[i]):
					_dist = [dist([x[i], y[i]], [x[j], y[j]]), dist([x[j], y[j]], [x[k], y[k]]), dist([x[k], y[k]], [x[i], y[i]])]
					_dist.sort()
					if _dist[0]*_dist[1] > _max: _max = _dist[0]*_dist[1]
print(int(_max))
