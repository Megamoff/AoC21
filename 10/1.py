data = open("input.txt").read().split("\n")[:-1]

score = 0
for i in data:
	stack = []
	for j in i:
		if j == "(" or j == "[" or j == "{" or j == "<":
			stack.append(j)
		if j == ")" or j == "]" or j == "}" or j == ">":
			if len(stack) == 0:
				break
			c = stack.pop()
			if j == ")" and not c == "(":
#				data.remove(i)
				score += 3
				break
			if j == "]" and not c == "[":
#				data.remove(i)
				score += 57
				break
			if j == "}" and not c == "{":
#				data.remove(i)
				score += 1197
				break
			if j == ">" and not c == "<":
#				data.remove(i)
				score += 25137
				break
#print(data)
	print(score)
				
