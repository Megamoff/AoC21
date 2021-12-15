data = open("input.txt").read().split(",")

map = [0]*9
for i in data:
	map[int(i) +1] += 1

for i in range(257):
	n = map[0]
	for j in range(len(map) -1):
		map[j] = map[j+1]
	map[6] += n
	map[8] = n
	
print(sum(map))
