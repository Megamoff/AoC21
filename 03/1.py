data = open("input.txt").read().split("\n")[:-1]

rate = ""
for i in range(len(data[0])):
	c = sum([j[i] == "1" for j in data])
	rate = rate + ("1" if c > len(data)/2 else "0")
inv_rate = "".join("1" if i == "0" else "0" for i in rate)

print(int(rate, 2) * int(inv_rate,2))
