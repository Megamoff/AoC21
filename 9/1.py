data = open("input.txt").read().split("\n")[:-1]

map = []
for i in data:
	map.append([int(j) for j in i])

sum = 0
for i in range(len(map)):
	for j in range(len(map[i])):
		if i > 0 and map[i-1][j] <= map[i][j]:
			continue
		if i < len(map)-1 and map[i+1][j] <= map[i][j]:
			continue
		if j > 0 and map[i][j-1] <= map[i][j]:
			continue
		if j < len(map[i])-1 and map[i][j+1] <= map[i][j]:
			continue
		sum += map[i][j]
		sum += 1
print(sum)
