s = input().lower()
x = ''
for i in range(len(s)):
    if s[i] != 'a' and s[i] != 'e' and s[i] != 'i' and s[i] != 'o' and s[i] != 'u' and s[i] != 'y':
        x += s[i]
for i in x:
    print('.'+i, end='')
