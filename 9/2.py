data = open("input.txt").read().split("\n")[:-1]

map = []
for i in data:
	map.append([int(j) for j in i])

def deep_search(i, j):
	if map[i][j] == 9:
		return 0
	map[i][j] = 9
	n = 1
	if i > 0:
		n += deep_search(i-1, j)
	if j > 0:
		n += deep_search(i, j -1)
	if i < len(map)-1:
		n += deep_search(i+1, j)
	if j < len(map[i])-1:
		n += deep_search(i, j+1)
	return n

basins = []
for i in range(len(map)):
	for j in range(len(map[i])):
		if map[i][j] != 9:
			basins.append(deep_search(i,j))
print(sorted(basins)[-3:])
