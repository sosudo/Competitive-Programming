import sys
sys.stdin = open("square.in", "r")
sys.stdout = open("square.out", "w")
ox1, oy1, ox2, oy2 = map(int, input().split())
tx1, ty1, tx2, ty2 = map(int, input().split())
print(max((max(ox2, tx2) - min(ox1, tx1)), (max(oy2, ty2) - min(oy1, ty1)))**2)
