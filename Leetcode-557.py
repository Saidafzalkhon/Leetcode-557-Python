s = input()
r = s.split()
s = ''
for i in r:
    s+= ''.join(i[::-1])
    s+=' '
print(s.strip())