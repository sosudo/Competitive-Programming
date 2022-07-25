n = int(input())
x = list(map(int, input().split()))
a = 0
l = 1
for i in range(n-1):
    if x[i+1] >= x[i]:
        l += 1
    else:
        a = max(l, a)
        l = 1
print(max(l, a))
