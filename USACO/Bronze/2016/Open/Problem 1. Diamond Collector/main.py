import sys
sys.stdin = open('diamond.in', 'r');sys.stdout = open('diamond.out', 'w')
n, k = map(int, input().split())
c = []
for _ in range(n):
    c.append(int(input()))
ans = 0
for i in range(n):
    amt = 0
    for j in range(n):
        if c[j] >= c[i] and c[j] <= c[i] + k:
            amt += 1
    if amt > ans:
        ans = amt
print(ans)
