t = int(input())
out = ''
for _ in range(t):
    n, x = map(int, input().split())
    nt = list(map(int, input().split()))
    nt.sort()
    n1 = [nt[i] for i in range(n)]
    n2 = [nt[i] for i in range(n, 2*n)]
    ans = "YES"
    for i in range(n):
        if n2[i] < n1[i] + x:
            ans = "NO"
            break
    out += ans + "\n"
print(out[:-1], end='')
