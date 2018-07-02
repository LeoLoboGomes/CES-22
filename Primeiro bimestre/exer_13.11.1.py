file = open("test.txt", "r")
reverse_file = open ("reverse test.txt", "w")
lines = []
while True:
    theline = file.readline()
    if len(theline) == 0:
        break
    lines.append(theline)
for i in range(len(lines)):
    if i == 0:
        reverse_file.write(lines[len(lines) - i - 1] + "\n")
    else:
        reverse_file.write(lines[len(lines) - i - 1])
file.close()
reverse_file.close()