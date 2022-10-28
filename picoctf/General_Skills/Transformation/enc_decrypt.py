"""8 to 16 bit binary"""

enc = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弲㘶㠴挲ぽ"
poo = []
wee = []
for char in enc:
    if len(bin(ord(char))) == 17:
        poo.append(bin(ord(char))[:9])
        poo.append(bin(ord(char))[9:])
    else:
        poo.append(bin(ord(char))[:8])
        poo.append(bin(ord(char))[9:])
    
for char in poo:
    wee.append(chr(int(char, 2)))
print(wee)

for item in wee:
    print(item, end='')