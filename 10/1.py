data = open("input.txt").read().split("\n")[:-1]

score = 0
for i in data:
	stack = []
	for j in i:
		if j == "(" or j == "[" or j == "{" or j == "<":
			stack.append(j)
		if j == ")" and not stack.pop() == "(":
			score += 3
			break
		if j == "]" and not stack.pop() == "[":
			score += 57
			break
		if j == "}" and not stack.pop() == "{":
			score += 1197
			break
		if j == ">" and not stack.pop() == "<":
			score += 25137
			break
print(score)
				
