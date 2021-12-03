data = open("input.txt").read().split("\n")[:-1]

rate = ""

for i in range(len(data[0])):
	c = 0
	for k in range(len(data)):
		if data[k][i] == "1":
			c += 1
	if c > len(data)/2:
		rate = rate + "1"
	else:
		rate = rate + "0"

print(rate)
