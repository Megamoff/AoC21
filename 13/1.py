data = open("input.txt").read().replace("fold along ", "").split("\n\n")#[:-1]

map = [[" "]*1500 for x in range(1500)]

for i in data[0].split("\n"):
	x, y = i.split(",")
	map[int(x)][int(y)] = "#"

for i in data[1].split("\n")[:-1]:
	i = i.split("=")
	i[1] = int(i[1])
	if "x" in i[0]:
		for j in range(len(map)):
			if j + i[1] >= len(map) or i[1] -j < 0:
				break
			for k in range(len(map[0])):
				if map[i[1] +j][k] == "#":
					map[i[1] -j][k] = "#"
		map = map[:i[1]]
	
	if "y" in i[0]:
		for j in range(len(map[0])):
			if j + i[1] >= len(map[0]) or i[1] -j < 0:
				break
			for k in range(len(map)):
				if map[k][i[1] +j] == "#":
					map[k][i[1] -j] = "#"
		for j in range(len(map)):
			map[j] = map[j][:i[1]]
			
map = list(map[::-1])
map = list(zip(*map[::-1]))
#map = list(zip(*map[::-1]))
print(str(map)[2:-2].replace("), (", "\n").replace("\', \'", ""))
print(sum(j == "#" for i in map for j in i))
