pad = {
	(0, 0): 1,
	(0, 1): 2,
	(0, 2): 3,
	(1, 0): 4,
	(1, 1): 5,
	(1, 2): 6,
	(2, 0): 7,
	(2, 1): 8,
	(2, 2): 9
}

new_pad = {
	(0, 0): 2,
	(0, 1): 3,
	(0, 2): 4,
	(1, 0): 6,
	(1, 1): 7,
	(1, 2): 8,
	(2, 0): 'A',
	(2, 1): 'B',
	(2, 2): 'C',
	(-1, 1): 1,
	(1, -1): 5,
	(3, 1): 'D',
	(1, 3): 9
}

actions = {
	'U': lambda row, col: (row-1, col),
	'D': lambda row, col: (row+1, col),
	'L': lambda row, col: (row, col-1),
	'R': lambda row, col: (row, col+1)
}

def is_valid(row, col, new):
	if not new:
		if row in range(0, 3) and col in range(0, 3):
			return True
	else:
		if (row in range(0, 3) and col in range(0, 3)) or (row, col) in [(-1, 1), (1, -1), (3, 1), (1, 3)]:
			return True

	return False

def get_code(start, instructions, new):
	code_coords = []
	coord = start

	for line in instructions:
		for instr in line:
			new_row, new_col = actions[instr](*coord)
			if is_valid(new_row, new_col, new):
				coord = (new_row, new_col)
		code_coords.append(coord)

	if not new:
		code = [str(pad[c]) for c in code_coords]
	else:
		code = [str(new_pad[c]) for c in code_coords]
	return ''.join(code)


if __name__ == '__main__':
	with open('input', 'r') as f:
		instructions = [line.strip('\n') for line in  f.readlines()]

	code = get_code((1, 1), instructions, new=False)
	print code
	code = get_code((1, -1), instructions, new=True)
	print code