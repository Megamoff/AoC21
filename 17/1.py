target_x = range(138, 185)
target_y = range(-125, -70)

max_y = 0

def shot(v_x, v_y):
	global max_y
	x = 0
	y = 0
	
	h = max_y
	while x < max(target_x) and y > min(target_y):
		if v_y == 0 and y > h:
			h = y
		x += v_x
		y += v_y
		
		if v_x > 0:
			v_x -= 1
		v_y -= 1
		
		if x in target_x and y in target_y:
			max_y = h
			return True
	return False

res_x = 0
while not shot(res_x, 0):
	res_x += 1
for i in range(res_x):
	res_y = 0
	print(res_x -i)
	while res_y < 500:
		shot(res_x -i, res_y)
		res_y += 1
print(max_y)
