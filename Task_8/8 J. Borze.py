s = input()
i = 0
z = ""

while i < len(s):
    if s[i] == '.':
        z += "0"
        i += 1
    else:
        if s[i+1] == '.':
            z += "1"
        else:
            z += "2"
        i += 2
print(z)