t = int(input())
for _ in range(t):
    a = int(input())
    n = -360/(a-180)
    if n >= 3 and n.is_integer():
        print("YES")
    else:
        print("NO")
