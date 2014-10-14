import fileinput

line_array = []
for line in fileinput.input():
    line_array.append(int(line))


