file = open("input.txt", "r")
data = file.read()[:-1].split("\n")

counter = 0

for i in range(len(data)):
	data[i] = int(data[i])

slide = []
for i in range(len(data)-2):
	slide.append(data[i] + data[i+1] + data[i+2])
	if i > 0 and slide[i] > slide[i-1]:
		counter += 1


print(counter)

