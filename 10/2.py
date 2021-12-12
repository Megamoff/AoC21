data = open("input.txt").read().split("\n")[:-1]

score = []
for i in data:
	stack = []
	b = False
	for j in i:
		if j == "(" or j == "[" or j == "{" or j == "<":
			stack.append(j)
		if j == ")" and not stack.pop() == "(":
			b = True
			break
		if j == "]" and not stack.pop() == "[":
			b = True
			break
		if j == "}" and not stack.pop() == "{":
			b = True
			break
		if j == ">" and not stack.pop() == "<":
			b = True
			break
	if b:
		continue
	s = 0
	while len(stack) > 0:
		c = stack.pop()
		s *= 5
		s += 1
		if c == "[":
			s += 1
		if c == "{":
			s += 2
		if c == "<":
			s += 3
	score.append(s)
		
score = sorted(score)
print(score[int(len(score)/2)])
				
