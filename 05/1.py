data = open("input.txt").read().replace(" -> ", ",").split("\n")[:-1]

map = [[0]*1000 for x in range(1000)]

for i in data:
	pos = i.split(",")
	if int(pos[0]) != int(pos[2]) and int(pos[1]) != int(pos[3]):
		continue
		
	if int(pos[0]) > int(pos[2]):
		pos[0], pos[2] = pos[2], pos[0]
	if int(pos[1]) > int(pos[3]):
		pos[1], pos[3] = pos[3], pos[1]
		
	for k in range(int(pos[0]), int(pos[2]) +1):
		for j in range(int(pos[1]), int(pos[3]) +1):
			map[k][j] += 1
print(sum(j > 1 for i in map for j in i))
