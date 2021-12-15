data = open("input.txt").read().replace(" -> ", "").split("\n\n")

polymer = data[0]

rules = data[1].split("\n")[:-1]
for k in range(10):
	new = polymer[0]
	for i in range(len(polymer) -1):
		for j in rules:
			if polymer[i] == j[0] and polymer[i+1] == j[1]:
				new = new + j[2]
				new = new + j[1]
	polymer = new

count = {}
for i in polymer:
	count[i] = 0
for i in polymer:
	count[i] += 1

print(count)
