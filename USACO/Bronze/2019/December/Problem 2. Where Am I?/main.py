import sys
sys.stdin = open('whereami.in', 'r')
sys.stdout = open('whereami.out', 'w')
def counter(word, sub):
    c = 0
    l = len(sub)
    w = len(word)
    for i in range(w-l+1):
        if word[i:i+l] == sub:
            c += 1
    return c
L = int(input())
N = input()
a = []
for i in range(1, L+1):
	for j in range(L):
	    a.append(N[j:i+j])
	check = N[0:i]
	end = True
	for j in a[0:L-i+1]:
	    if counter(N, j) != 1:
	        end = False
	        break
	if end:
	    print(i)
	    break
	a = []
