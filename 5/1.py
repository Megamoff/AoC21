data = open("input.txt").read().replace(" -> ", ",").split("\n")[:-1]

map = []
for i in range(1000):
	map.append([])
	for j in range(1000):
		map[i].append(0)

for i in data:
	pos = i.split(",")
	if int(pos[0]) != int(pos[2]) and int(pos[1]) != int(pos[3]):
		continue
		
	if int(pos[0]) > int(pos[2]):
		h = pos[0]
		pos[0] = pos[2]
		pos[2] = h
	if int(pos[1]) > int(pos[3]):
		h = pos[1]
		pos[1] = pos[3]
		pos[3] = h
		
	for k in range(int(pos[0]), int(pos[2]) +1):
		for j in range(int(pos[1]), int(pos[3]) +1):
			map[k][j] += 1

counter = 0
for i in range(1000):
	for j in range(1000):
		if map[i][j] > 1:
			counter += 1

print(counter)
