data = open("input.txt").read()

data = bin(int(data, 16))[2:]
i = 0

versions = []

def process():
	global i
	if i >= len(data):
		return
	versions.append(int(data[i: i+3], 2))
	type = int(data[i+3: i+6], 2)
	i += 6
	
	if type == 4:
		n = 0
		while data[i] == "1":
			n += int(data[i +1: i +5], 2)
			i += 5
		n += int(data[i +1: i +5], 2)
		i += 5
		return n
	else:
		if data[i] == "0":
			bits = int(data[i +1: i +16], 2)
			i += 16
			
			bits += i
			while i < bits:
				process()
		else:
			bits = int(data[i +1: i +12], 2)
			i += 12
			
			for j in range(bits):
				process()

while i < len(data) -1:
	if int(data[i:]) == 0:
		break
	process()

print(sum(versions))
