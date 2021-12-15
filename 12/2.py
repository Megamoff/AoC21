import copy

data = open("input.txt").read().split("\n")[:-1]

nodes = []

for i in data:
	edge = i.split("-")
	n1 = -1
	n2 = -1
	for j in range(len(nodes)):
		if edge[0] == nodes[j][0]:
			n1 = j
		if edge[1] == nodes[j][0]:
			n2 = j
	if n1 == -1:
		nodes.append([edge[0]])
		n1 = len(nodes) -1
	if n2 == -1:
		nodes.append([edge[1]])
		n2 = len(nodes) -1
	nodes[n1].append(edge[1])
	nodes[n2].append(edge[0])
nodes = sorted(nodes)

def deep_search(n, path, revisited):
	if n == "end":
		return 1
	if n == "start" and not len(path) == 0:
		return 0
	
	adjacentNodes = []
	for i in range(len(nodes)):
		if nodes[i][0] == n:
			adjacentNodes = copy.deepcopy(nodes[i][1:])
			break
	new = []
	for i in adjacentNodes:
		if i.isupper() or i not in path or not revisited:
			new.append(i)
	adjacentNodes = sorted(set(new))
	
	number = 0
	new = copy.deepcopy(path)
	new.append(n)
	for i in adjacentNodes:
		if i in new and i.islower():
			number += deep_search(i, new, True)
		else:
			number += deep_search(i, new, revisited)
	return number

s = deep_search("start", [], False)
print(s)
