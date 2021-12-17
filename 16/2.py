from math import prod

data = open("input.txt").read()

data = bin(int(data, 16))[2:]
i = 0

versions = []

def process():
	global i
	if i >= len(data):
		return
#	versions.append(int(data[i: i+3], 2))
	type = int(data[i+3: i+6], 2)
	i += 6
	
	if type == 4:
		n = ""
		while data[i] == "1":
			n = n + data[i +1: i +5]
			i += 5
		n = n + data[i +1: i +5]
		i += 5
		return int(n, 2)
	else:
		packets = []
		if data[i] == "0":
			bits = int(data[i +1: i +16], 2)
			i += 16
			
			bits += i
			while i < bits:
				packets.append(process())
		else:
			bits = int(data[i +1: i +12], 2)
			i += 12
			
			for j in range(bits):
				packets.append(process())
		
		if type == 0:
			return sum(packets)
		if type == 1:
			return prod(packets)
		if type == 2:
			return min(packets)
		if type == 3:
			return max(packets)
		if type == 5:
			return 1 if packets[0] > packets[1] else 0
		if type == 6:
			return 1 if packets[0] < packets[1] else 0
		if type == 7:
			return 1 if packets[0] == packets[1] else 0

print(process())
