x, y = 0, 0
for i in range(5):
    z = list(map(int, input().split()))
    if 1 in z:
        x = i
        y = z.index(1)
print(abs(2-x)+abs(2-y))
