import sys
sys.stdin = open('shell.in', 'r')
sys.stdout = open('shell.out', 'w')
n = int(input())
a = [1, 0, 0]
b = [0, 1, 0]
c = [0, 0, 1]
p1 = 0
p2 = 0
p3 = 0
def swap(x, y, z):
	tmp = x[y-1]
	x[y-1] = x[z-1]
	x[z-1] = tmp
for i in range(n):
	A, B, G = list(map(int, input().split()))
	swap(a, A, B)
	swap(b, A, B)
	swap(c, A, B)
	if a[G-1] == 1:
		p1 += 1
	if b[G-1] == 1:
		p2 += 1
	if c[G-1] == 1:
		p3 += 1
print(max(p1, p2, p3))
