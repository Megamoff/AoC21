co2 = open("input.txt").read().split("\n")[:-1]
oxgen = open("input.txt").read().split("\n")[:-1]

for i in range(len(oxgen[0])):
	c = sum([j[i] == "1" for j in oxgen])
	oxgen = [j for j in oxgen if (c >= len(oxgen)/2 and j[i] == "1") or (c < len(oxgen)/2 and j[i] == "0")]

for i in range(len(co2[0])):
	c = sum([j[i] == "1" for j in co2])
	co2 = [j for j in co2 if (c < len(co2)/2 and j[i] == "1") or (c >= len(co2)/2 and j[i] == "0")]
	if len(co2) == 1:
		break

print(int(co2[0], 2) * int(oxgen[0],2))
