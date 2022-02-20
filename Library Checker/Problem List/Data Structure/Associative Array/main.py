a = {}
for i in range(int(input())):
    _in = [int(i) for i in input().split()]
    if _in[0] == 0:
        a[_in[1]] = _in[2]
    if _in[0] == 1:
        try:
            print(a[_in[1]])
        except:
            print(0)
