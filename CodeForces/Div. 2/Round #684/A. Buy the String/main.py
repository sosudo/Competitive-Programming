t = int(input())
out = ''
for i in range(t):
    n, c0, c1, h = map(int, input().split())
    s = input()
    ans = 0
    for i in s:
        ans += c0 if i == '0' else c1
    if c0 < c1:
        ans = min(ans, ans-s.count('1')*c1+s.count('1')*h+s.count('1')*c0)
    else:
        ans = min(ans, ans-s.count('0')*c0+s.count('0')*h+s.count('0')*c1)
    out += str(ans) + "\n"
print(out)
