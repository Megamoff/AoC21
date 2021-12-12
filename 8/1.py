data = open("input.txt").read().replace(" |", "").split("\n")

counter = 0
for i in data:
	for j in i.split(" ")[10:]:
		if len(j) == 2 or len(j) == 3 or len(j) == 4 or len(j) == 7:
			counter += 1
print(counter)
