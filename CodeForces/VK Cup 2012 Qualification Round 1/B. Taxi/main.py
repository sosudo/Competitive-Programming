from math import ceil
n = int(input())
s = list(map(int, input().split()))
d = {
    1: s.count(1),
    2: s.count(2),
    3: s.count(3),
    4: s.count(4)
}
ans = d[4]
d[4] = 0
m1 = min(d[1], d[3])
d[1] -= m1
d[3] -= m1
ans += m1
if d[3] > 0 and d[1] <= 0:
    ans += d[3]
    ans += ceil(d[2]/2)
elif d[3] <= 0 and d[1] > 0:
    z = int(d[1]//2)
    d[2] += z
    d[1] -= 2*z
    m2 = min(d[1], d[2])
    ans += m2
    d[1] -= m2
    d[2] -= m2
    if d[1] > 0 and d[2] <= 0:
        ans += ceil(d[1]/4)
    elif d[1] <= 0 and d[2] > 0:
        ans += ceil(d[2]/2)
elif d[3] == 0 and d[1] == 0:
    ans += ceil(d[2]/2)
print(ans)
