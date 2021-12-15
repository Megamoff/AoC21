data = open("input.txt").read().replace(" -> ", ",").split("\n")[:-1]

map = [[0]*1000 for x in range(1000)]

for i in data:
	pos = i.split(",")
	for i in range(len(pos)):
		pos[i] = int(pos[i])
		
	if pos[0] == pos[2] or pos[1] == pos[3]:
		if pos[0] > pos[2]:
			pos[0], pos[2] = pos[2], pos[0]
		if pos[1] > pos[3]:
			pos[1], pos[3] = pos[3], pos[1]
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
print(sum(j > 1 for i in map for j in i))
