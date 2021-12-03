file = open("input.txt", "r")
data = file.read()[:-1].split("\n")

pos = 0
depth = 0

for i in range(len(data)):
	data[i] = data[i].split(" ")
	data[i][1] = int(data[i][1])
	if data[i][0] == "down":
		depth += data[i][1]
	if data[i][0] == "up":
		depth -= data[i][1]
	if data[i][0] == "forward":
		pos += data[i][1]

print(str(pos*depth))
