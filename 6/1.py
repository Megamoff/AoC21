data = open("input.txt").read().split(",")

map = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in data:
	map[int(i) +1] += 1

for i in range(257):
	n = map[0]
	for j in range(len(map) -1):
		map[j] = map[j+1]
	map[6] += n
	map[8] = n
	print(map)

c = 0
for i in map:
	c += int(i)
	
print(c)
