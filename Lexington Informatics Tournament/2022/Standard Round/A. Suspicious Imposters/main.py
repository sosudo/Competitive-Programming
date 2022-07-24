N, M = map(int, input().split())
out = {}
for i in range(N):
    s = input()
    x = [int(i) for i in s]
    out[s] = sum(x) % 13
out = dict(sorted(out.items(), key=lambda x: (x[1],x[0]), reverse=True))
z = list(out.keys())
for i in range(M):
    print(z[i])
