import sys
sys.stdin = open("cowsignal.in", "r")
sys.stdout = open("cowsignal.out", "w")
M, N, K = map(int, input().split())
amp = []
for _ in range(M):
    signal = input()
    amped = ''
    for i in signal:
        amped += K*i
    [amp.append(amped) for _ in range(K)]
print(*amp, sep="\n")
