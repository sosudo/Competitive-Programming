import sys
sys.stdin = open("mixmilk.in", 'r')
sys.stdout = open("mixmilk.out", 'w')
capacity = []
prev = [0, 0, 0]
curr = []
pour = 0
repeater = 0
for i in range(3):
	x = input().split()
	capacity.append(int(x[0]))
	curr.append(int(x[1]))
for i in range(100):
	if pour == 0:
		_sum = curr[0] + curr[1]
		rem = _sum - capacity[1]
		curr[0] = rem if rem >= 0 else 0
		curr[1] = _sum - curr[0]
	elif pour == 1:
		_sum = curr[1] + curr[2]
		rem = _sum - capacity[2]
		curr[1] = rem if rem >= 0 else 0
		curr[2] = _sum - curr[1]
	elif pour == 2:
		_sum = curr[2] + curr[0]
		rem = _sum - capacity[0]
		curr[2] = rem if rem >= 0 else 0
		curr[0] = _sum - curr[2]
	else:
		break
	prev[0] = curr[0]
	prev[1] = curr[1]
	prev[2] = curr[2]
	pour = 0 if pour == 2 else pour+1
	if prev[0] == curr[0] and prev[1] == curr[1] and prev[2] == curr[2]:
		repeater += 1
	if repeater == 4:
		break
print(curr[0])
print(curr[1])
print(curr[2])
