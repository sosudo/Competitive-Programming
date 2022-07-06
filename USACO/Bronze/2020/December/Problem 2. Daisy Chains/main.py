N = int(input())
p = input("").split()
p = [int(i) for i in p]
x = [i for i in p]
ans = N
for j in range(N-1):
	for i in range(N-1):
		if len(x) != 1:
			avg = sum(x)/len(x)
			if avg in x:
				ans += 1
			x.pop(0)
	x = [i for i in p]
	[x.pop() for r in range(j+1)]
print(ans)
