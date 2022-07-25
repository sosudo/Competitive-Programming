n = int(input())
x = list(map(int, input().split()))
a1 = x.index(max(x)) + 1
a2 = sorted(set(x))[-2]
print(a1, a2)
