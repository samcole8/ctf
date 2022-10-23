text = ""
with open("command_output.txt","r") as f:
    file = f.read().splitlines()
for line in file:
    text = text + chr(int(line))
print(text)