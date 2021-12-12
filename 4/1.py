data = open("input.txt").read().replace("\n ", "\n").replace("  ", " ").split("\n\n")[:-1]

boards = []
numbers = data[0].split(",")[:-1]

for i in range(1, len(data)):
#	boards.append(" " + data[i].replace("\n", " ").replace("  ", " ") + " ")
	board = []
	a = data[i].split("\n")
	for j in range(5):
		board.append([])
		b = a.split(" ")
		for k in range(5):
			board[j].append(int(b[k]))

def main():
	for i in numbers:
		for j in range(len(boards)):
			board = boards[j]
			

main()
