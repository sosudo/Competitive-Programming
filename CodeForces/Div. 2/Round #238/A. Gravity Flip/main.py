n = int(input())
cols = list(map(int, input().split()))[::-1]
m = max(cols)
x = []
for i in range(n):
    x.append([1 for j in range(cols[i])])
    x[i] += [0 for j in range(m-cols[i])]
x = sorted(x, key=lambda i: i.count(0), reverse = True)
for i in range(len(x)-1):
    for j in range(m):
        if x[i+1][j] == 0 and x[i][j] == 1:
            x[i+1][j] = 1
            x[i][j] = 0
    print(x[i].count(1), end = ' ')
print(x[-1].count(1))
