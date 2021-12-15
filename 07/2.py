data = open("input.txt").read().split(",")

pos = [0]*2000
for i in data:
	pos[int(i)] += 1

low = 1000000000000
for j in range(len(pos)):
	res = 0
	for i in range(len(pos)):
		res += pos[i] * abs(i-j)*(abs(i-j)+1)/2
	if res < low:
		low = res
	else:
		break
print(int(low))
