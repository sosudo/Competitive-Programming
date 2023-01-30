import sys
sys.stdin = open('pails.in', 'r')
sys.stdout = open('pails.out', 'w')
x, y, m = map(int, input().split())
limx = m//x
limy = m//y
_max = 0
for i in range(1, limx+1):
    _max = max(_max, x*i+((m-x*i)//y)*y)
for i in range(1, limy+1):
    _max = max(_max, y*i+((m-y*i)//x)*x)
print(_max)
