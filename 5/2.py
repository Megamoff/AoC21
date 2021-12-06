data = open("input.txt").read().replace(" -> ", ",").split("\n")[:-1]

map = []
for i in range(1000):
	map.append([])
	for j in range(1000):
		map[i].append(0)

for i in data:
	pos = i.split(",")
	for i in range(len(pos)):
		pos[i] = int(pos[i])
		
	if pos[0] == pos[2] or pos[1] == pos[3]:
		if pos[0] > pos[2]:
			h = pos[0]
			pos[0] = pos[2]
			pos[2] = h
		if pos[1] > pos[3]:
			h = pos[1]
			pos[1] = pos[3]
			pos[3] = h
		for k in range(pos[0], pos[2] +1):
			for j in range(pos[1], pos[3] +1):
				map[k][j] += 1
	elif pos[0] > pos[2]:
		if pos[1] > pos[3]:
			for j in range(pos[1]-pos[3] +1):
				map[pos[0] -j][pos[1] -j] += 1
		else:
			for j in range(pos[3]-pos[1] +1):
				map[pos[0] -j][pos[1] +j] += 1
	else:
		if pos[1] > pos[3]:
			for j in range(pos[1]-pos[3] +1):
				map[pos[0] +j][pos[1] -j] += 1
		else:
			for j in range(pos[3]-pos[1] +1):
				map[pos[0] +j][pos[1] +j] += 1
		

counter = 0
for i in range(1000):
	for j in range(1000):
		if map[i][j] > 1:
			counter += 1

print(counter)
