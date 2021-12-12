data = open("input.txt").read().replace(" |", "").split("\n")[:-1]
digits = ["023456", "25", "02346", "02356", "1235", "01356", "013456", "025", "0123456", "012356"]

def part(poss, x):
	newPoss = ""
	for i in poss:
		if i in x:
			newPoss = newPoss + i
	return newPoss
	
def notPart(poss, x):
	newPoss = ""
	for i in poss:
		if not i in x:
			newPoss = newPoss + i
	return newPoss
	
def update(res, n, input):
	for k in range(7):
		if str(k) in digits[n]:
			res[k] = part(res[k], input)
		else:
			res[k] = notPart(res[k], input)
	return res

sum = 0
for i in data:
	input = i.split(" ")
	res = ["abcdefg"]*7
	for j in range(len(input)):
		if len(input[j]) == 2:
			update(res, 1, input[j])
		if len(input[j]) == 3:
			update(res, 7, input[j])
		if len(input[j]) == 4:
			update(res, 4, input[j])
		if len(input[j]) == 5:
			newPoss = ""
			for k in res[3]:
				if k in input[j]:
					newPoss = newPoss + k
			res[3] = newPoss
		if len(input[j]) == 6:
			newPoss = ""
			for k in res[6]:
				if k in input[j]:
					newPoss = newPoss + k
			res[6] = newPoss
			newPoss = ""
			for k in res[5]:
				if k in input[j]:
					newPoss = newPoss + k
			res[5] = newPoss
	
	for j in range(len(res)):
		if len(res[j]) == 1:
			for k in range(len(res)):
				if len(res[k]) != 1:
					newPoss = ""
					for l in res[k]:
						if not l in res[j]:
							newPoss = newPoss + l
					res[k] = newPoss
	
	for j in range(len(input)):
		new = ""
		for k in range(len(input[j])):
			pos = res.index(input[j][k])
			new = new + chr(pos +97)
		input[j] = "".join(sorted(new))

		if input[j] == "abcefg":
			input[j] = 0
		if input[j] == "cf":
			input[j] = 1
		if input[j] == "acdeg":
			input[j] = 2
		if input[j] == "acdfg":
			input[j] = 3
		if input[j] == "bcdf":
			input[j] = 4
		if input[j] == "abdfg":
			input[j] = 5
		if input[j] == "abdefg":
			input[j] = 6
		if input[j] == "acf":
			input[j] = 7
		if input[j] == "abcdefg":
			input[j] = 8
		if input[j] == "abcdfg":
			input[j] = 9
	
	sum += input[10] * 1000 + input[11] * 100 + input[12] * 10 + input[13]
print(sum)
