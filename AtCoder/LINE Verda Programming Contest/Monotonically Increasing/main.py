from itertools import permutations
n, m = map(int, input().split())
x = [i+1 for i in range(m)]
for i in permutations(x, n):
    if all(x<y for x, y in zip(i, i[1:])):
        print(*i)
