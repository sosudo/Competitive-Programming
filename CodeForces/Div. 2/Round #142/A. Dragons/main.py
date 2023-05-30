s, n = map(int, input().split())
d = []
for _ in range(n):
    x, y = map(int, input().split())
    d.append((x,y))
d = sorted(d)
for i in d:
    if s <= i[0]:
        print("NO")
        exit(0)
    else:
        s += i[1]
print("YES")
