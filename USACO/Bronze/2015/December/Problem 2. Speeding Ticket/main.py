import sys
sys.stdin = open('speeding.in', 'r')
sys.stdout = open('speeding.out', 'w')
n, m = list(map(int, input().split()))
b = []
a = []
for i in range(n):
	d, l = list(map(int, input().split()))
	[b.append(l) for _ in range(d)]
for i in range(m):
	d, l = list(map(int, input().split()))
	[a.append(l) for _ in range(d)]
ans = 0
for i in range(min(len(a), len(b))):
	ans = max(ans, a[i]-b[i])
print(ans) 
