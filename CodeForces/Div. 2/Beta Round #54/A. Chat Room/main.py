s = input()
x = 'a'
for i in s:
    if i == 'h':
        if x.count(i) < 1:
            x += i
    if i == 'e':
        if x.count(i) < 1 and x[-1] == 'h':
            x += i
    if i == 'l':
        if x.count(i) < 2 and (x[-1] == 'e' or x[-1] == 'l'):
            x += i
    if i == 'o':
        if x.count(i) < 1 and x[-1] == 'l' and x[-2] == 'l':
            x += i
if x == 'ahello':
    print("YES")
else:
    print("NO")
