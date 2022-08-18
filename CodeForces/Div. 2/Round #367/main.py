def search(x, val, low, high, previdx):
    idx = int((high+low)//2)
    if low > high:
        return previdx
    if val >= x[idx]:
        return search(x, val, idx+1, high, idx+1)
    if val < x[idx]:
        return search(x, val, low, idx-1, idx)
n = int(input())
x = list(map(int, input().split()))
x.sort()
q = int(input())
for _ in range(q):
    m = int(input())
    if m < x[0]:
        print(0)
    elif m >= x[-1]:
        print(n)
    else:
        print(search(x, m, 0, n, n//2))
