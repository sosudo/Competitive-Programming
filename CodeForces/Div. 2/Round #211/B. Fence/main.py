n, k = map(int, input().split())
z = list(map(int, input().split()))
h = [0] + z
a = sum(h[1:k+1])
_min = sum(h[1:k+1])
idx = 1
for i in range(2, n-k+2):
    _min = _min - h[i-1] + h[k+i-1]
    if _min < a:
        a = _min
        idx = i
print(idx)
