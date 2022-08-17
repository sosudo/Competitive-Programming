t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    if n%2 == 1 and m%2 == 0:
        print("Burenka")
    elif n%2 == 0 and m%2 == 0:
        print("Tonya")
    elif n%2 == 1 and m%2 == 1:
        print("Tonya")
    elif n%2 == 0 and m%2 == 1:
        print("Burenka")
