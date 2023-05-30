z = input()
def iscaps(z):
    for i in z[1:]:
        if not i.isupper():
            return False
    return True
caps = iscaps(z)
if not caps:
    print(z)
else:
    out = ''
    for i in z:
        if i.islower():
            out += i.upper()
        else:
            out += i.lower()
    print(out)
