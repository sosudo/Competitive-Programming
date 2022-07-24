n, k = map(int, input().split())
b = list(map(int, input().split()))
c = b[k-1]
a = 0
for i in b:
    if i >= c and i > 0:
        a += 1
print(a)
