data = open("input.txt").read().split("\n")[:-1]
print(sum(int(data[i]) > int(data[i-1]) for i in range(1, len(data))))
