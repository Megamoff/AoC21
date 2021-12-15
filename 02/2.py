data = open("input.txt").read().split("\n")[:-1]

pos = depth = aim = 0

for i in data:
	i = i.split(" ")
	i[1] = int(i[1])
	if i[0] == "forward":
		pos += i[1]
		depth += aim * i[1]
	else:
		aim += i[1] if i[0] == "down" else -i[1]

print(pos*depth)
