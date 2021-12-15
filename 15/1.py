from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

data = open("input.txt").read().split("\n")[:-1]

map = []
for i in data:
	map.append([int(j) for j in i])

grid = Grid(matrix=map)
start = grid.node(0,0)
end = grid.node(len(map) -1, len(map[0]) -1)
finder = AStarFinder()
path, runs = finder.find_path(start, end, grid)

s = 0
for x, y in path[1:]:
	s += map[y][x]
#print('operations:', runs, 'path length:', len(path))
#print(grid.grid_str(path=path, start=start, end=end))
print(s)
