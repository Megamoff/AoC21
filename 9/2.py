data = open("input.txt").read().split("\n")[:-1]

map = []
for i in range(len(data)):
	map.append([])
	for j in data[i]:
		map[i].append(int(j))

def deep_search(i, j):
	if map[i][j] == 9:
		return 0
	map[i][j] = 9
	n = 1
	if i > 0:
		try:
			n += deep_search(i-1, j)
		except IndexError:
			pass
	if j > 0:
		try:
			n += deep_search(i, j -1)
		except IndexError:
			pass
	try:
		n += deep_search(i+1, j)
	except IndexError:
		pass
	try:
		n += deep_search(i, j+1)
	except IndexError:
		pass
	return n

basins = []
for i in range(len(map)):
	for j in range(len(map[i])):
		if map[i][j] == 9:
			continue
		basins.append(deep_search(i,j))
print(sorted(basins))
