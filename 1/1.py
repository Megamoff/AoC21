file = open("input.txt", "r")
data = file.read()[:-1].split("\n")

counter = 0

for i in range(len(data)):
	data[i] = int(data[i])
	if i > 0 and data[i] > data[i-1]:
		counter += 1

print(counter)

