import sys
sys.stdin = open("billboard.in", "r")
sys.stdout = open("billboard.out", "w")
board = [[0 for i in range(-1000, 1001)] for j in range(-1000, 1001)]
x1, y1, x2, y2 = map(int, input().split())
for i in range(x1, x2):
	for j in range(y1, y2):
		board[i][j] = 1
x1, y1, x2, y2 = map(int, input().split())
for i in range(x1, x2):
	for j in range(y1, y2):
		board[i][j] = 2
x1, y1, x2, y2 = map(int, input().split())
for i in range(x1, x2):
	for j in range(y1, y2):
		board[i][j] = 3
ans = 0
for i in board:
	ans += i.count(1)
	ans += i.count(2)
print(ans)
