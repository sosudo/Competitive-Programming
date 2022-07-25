n = int(input())
c = list(map(int, input().split()))
c.sort()
c = c[::-1]
s = 0
for i in range(len(c)):
    s += c[i]
    if s > sum(c[i+1:]):
        print(i+1)
        exit()
