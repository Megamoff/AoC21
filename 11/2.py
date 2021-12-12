data = open("input.txt").read().split("\n")[:-1]

map = []
for i in data:
	map.append([int(j) for j in i])

n = 0
for i in range(100000):
	for j in range(len(map)):
		for k in range(len(map[j])):
			map[j][k] += 1

	done = False
	while not done:
		done = True
		for j in range(len(map)):
			for k in range(len(map[j])):
				if map[j][k] > 9:
					done = False
					map[j][k] = -1000
					n += 1
					for l in range(-1, 2):
						for m in range(-1, 2):
							if j+l < 0 or k+m<0:
								continue
							try:
								map[j + l][k + m] += 1
							except IndexError:
								pass
	sync = True
	for j in range(len(map)):
		for k in range(len(map[j])):
			if map[j][k] < 0:
				map[j][k] = 0
			else:
				sync = False
	if sync:
		print(i +1)
		break
