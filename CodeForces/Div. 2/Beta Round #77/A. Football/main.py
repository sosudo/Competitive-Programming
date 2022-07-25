s = input()
for i in range(len(s)-6):
    if len(set(s[i:i+7])) == 1:
        print("YES")
        exit()
print("NO")
