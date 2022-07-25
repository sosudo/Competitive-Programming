from math import ceil
n, k = map(int, input().split())
k -= 1
odd_range = ceil(n/2)-1
even_range = n//2
if k <= odd_range:
    print(2*k+1)
    exit()
if n%2 == 0:
    print(2*(k-even_range+1))
else:
    print(2*(k-even_range))
