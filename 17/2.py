target_x = range(138, 185)
target_y = range(-125, -70)

v = set()

def shot(v_x, v_y):
	x = 0
	y = 0
	
	h_x = v_x
	h_y = v_y
	while x <= max(target_x) and y >= min(target_y):
		x += v_x
		y += v_y
		
		if v_x > 0:
			v_x -= 1
		v_y -= 1
		
		if x in target_x and y in target_y:
			v.add((h_x, h_y))
			return True
	return False

for i in range(186):
	for j in range(-125, 150):
#		print((i, j))
		shot(i, j)
print(len(v))
