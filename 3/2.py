data = open("input.txt").read().split("\n")[:-1]

rate = ""

for i in range(len(data[0])):
	c = 0
	for k in range(len(data)):
		if data[k][i] == "1":
			c += 1
	if c >= len(data)/2:
		rate = rate + "1"
	else:
		rate = rate + "0"


for i in range(len(data[0])):
	c = 0
	for k in range(len(data)):
		if data[k][i] == "1":
			c += 1
	new = []
	for k in range(len(data)):
		if (c < len(data)/2 and data[k][i] == "1") or (c >= len(data)/2 and data[k][i] == "0"):
			new.append(data[k])
	print(new)
	if len(new) == 1:
		break
	data = new
