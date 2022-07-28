from itertools import groupby
s = input()
groups = groupby(s)
x = [[label, sum(1 for _ in group)] for label, group in groups]
m = len(x)
ans = None
tmp = x[m//2][1]+1
if m % 2 == 0 or x[m//2][1] == 1 or [i[0] for i in x[::-1]] != [i[0] for i in x]:
    print(0)
    exit()
for i in range(len(x)//2):
    if [i[0] for i in x[::-1]] != [i[0] for i in x]:
        print(0)
        exit()
    else:
        while len(x) > 1:
            if x[0][1] + x[-1][1] > 2:
                del x[0]
                del x[-1]
            else:
                print(0)
                exit()
print(tmp if x[0][1] > 1 else 0)
