data = open("input.txt").read().split("\n")[:-1]
print(sum(int(data[i]) > int(data[i-3]) for i in range(3, len(data))))

