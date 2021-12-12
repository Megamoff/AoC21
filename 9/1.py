data = open("input.txt").read().split("\n")[:-1]

map = []
for i in range(len(data)):
	map.append([])
	for j in data[i]:
		map[i].append(int(j))

sum = 0
for i in range(len(map)):
	for j in range(len(map[i])):
		try:
			if map[i-1][j] <= map[i][j] and i > 0:
				continue
		except IndexError:
			pass
			
		try:
			if map[i+1][j] <= map[i][j]:
				continue
		except IndexError:
			pass
			
		try:
			if map[i][j-1] <= map[i][j] and j > 0:
				continue
		except IndexError:
			pass
			
		try:
			if map[i][j+1] <= map[i][j]:
				continue
		except IndexError:
			pass

		sum += map[i][j]
		sum += 1
print(sum)
