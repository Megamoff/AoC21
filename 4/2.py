data = open("input.txt").read().replace("\n ", "\n").split("\n\n")[:-1]

boards = []
numbers = data[0].split(",")[:-1]

for i in range(1, len(data)):
	boards.append(" " + data[i].replace("\n", " ").replace("  ", " ") + " ")

def main():
	global boards
	for i in numbers:
		newBoards = []
		for j in range(len(boards)):
			boards[j] = boards[j].replace(" " + str(i) + " ", " -1 ")
			
			board = boards[j].split(" ")[1:-1]
			win = False
			for k in range(0, 25, 5):
				if int(board[k]) + int(board[k+1]) + int(board[k+2]) + int(board[k+3]) + int(board[k+4]) == -5:
					win = True
			for k in range(5):
				if int(board[k]) + int(board[k+5]) + int(board[k+10]) + int(board[k+15]) + int(board[k+20]) == -5:
					win = True
			if not win:
				newBoards.append(boards[j])
		if len(newBoards) == 1:
			print(i)
			print(newBoards)
			return
		boards = newBoards

main()
