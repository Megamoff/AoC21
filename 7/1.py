data = open("input.txt").read().split(",")

pos = [0]*2000
for i in data:
	pos[int(i)] += 1

low = 100000000
for i in range(len(pos)):
	res = 0
	for j in range(len(pos)):
		res += pos[j] * abs(i - j)
	if res < low:
		low = res
	else:
		break
print(low)
