data = open("input.txt").read().replace(" -> ", "").split("\n\n")

rules = {}
for i in data[1].split("\n")[:-1]:
	pair_in = i[0] + i[1]
	pair_out1 = i[0] + i[2]
	pair_out2 = i[2] + i[1]
	rules[pair_in] = (pair_out1, pair_out2)

polymer = {}
for i in rules:
	polymer[i] = 0
for i in range(len(data[0]) -1):
	pair = data[0][i] + data[0][i+1]
	polymer[pair] += 1

for i in range(40):
	new = {}
	for j in polymer:
		new[j] = 0
	for j in rules:
		one, two = rules[j]
		new[one] += polymer[j]
		new[two] += polymer[j]
	polymer = new

count = {}
for i in polymer:
	count[i[0]] = 0
	count[i[1]] = 0
for i in polymer:
	count[i[0]] += polymer[i]
	count[i[1]] += polymer[i]
new = []
for i in count:
	new.append(count[i]/2)
count = sorted(new)
print(count)
