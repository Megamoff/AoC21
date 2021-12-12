data = open("input.txt").read().replace(" |", "").split("\n")

counter = 0
for i in data:
	for j in i.split(" ")[10:]:
		if len(j) in (2, 3, 4, 7):
			counter += 1
print(counter)
