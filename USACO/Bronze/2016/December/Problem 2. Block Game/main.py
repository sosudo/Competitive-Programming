import sys
sys.stdin = open('blocks.in', 'r')
sys.stdout = open('blocks.out', 'w')
n = int(input())
ans = [0 for i in range(26)]
for i in range(n):
	a = input().split()
	b = a[0]
	c = a[1]
	ans[0] += max(b.count('a'), c.count('a'))
	ans[1] += max(b.count('b'), c.count('b'))
	ans[2] += max(b.count('c'), c.count('c'))
	ans[3] += max(b.count('d'), c.count('d'))
	ans[4] += max(b.count('e'), c.count('e'))
	ans[5] += max(b.count('f'), c.count('f'))
	ans[6] += max(b.count('g'), c.count('g'))
	ans[7] += max(b.count('h'), c.count('h'))
	ans[8] += max(b.count('i'), c.count('i'))
	ans[9] += max(b.count('j'), c.count('j'))
	ans[10] += max(b.count('k'), c.count('k'))
	ans[11] += max(b.count('l'), c.count('l'))
	ans[12] += max(b.count('m'), c.count('m'))
	ans[13] += max(b.count('n'), c.count('n'))
	ans[14] += max(b.count('o'), c.count('o'))
	ans[15] += max(b.count('p'), c.count('p'))
	ans[16] += max(b.count('q'), c.count('q'))
	ans[17] += max(b.count('r'), c.count('r'))
	ans[18] += max(b.count('s'), c.count('s'))
	ans[19] += max(b.count('t'), c.count('t'))
	ans[20] += max(b.count('u'), c.count('u'))
	ans[21] += max(b.count('v'), c.count('v'))
	ans[22] += max(b.count('w'), c.count('w'))
	ans[23] += max(b.count('x'), c.count('x'))
	ans[24] += max(b.count('y'), c.count('y'))
	ans[25] += max(b.count('z'), c.count('z'))
print(*ans, sep='\n')
