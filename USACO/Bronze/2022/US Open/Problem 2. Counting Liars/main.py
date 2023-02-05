n = int(input())
ans = 100000000000000000
ins = []
for _ in range(n):
    ins.append(input().split())
for k in ins:
    i = int(k[1])
    tmp = 0
    for j in ins:
        j[1] = int(j[1])
        if j[0] == 'L':
            if i > j[1]:
                tmp += 1
        if j[0] == 'G':
            if i < j[1]:
                tmp += 1
    ans = min(tmp, ans)
print(ans)
