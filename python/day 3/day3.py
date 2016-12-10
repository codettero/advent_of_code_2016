def is_triange(sides):
	x, y, z = [int(n) for n in sides.split()]
	if x + y > z and y + z > x and x + z > y:
		return True

	return False

def transform(values):
	new_values = []
	for triplet in (values[i:i+3] for i in range(0, len(values), 3)):
		new_values.extend([' '.join([x.split()[0] for x in triplet]), ' '.join([x.split()[1] for x in triplet]), ' '.join(x.split()[2] for x in triplet)])

	return new_values

def count_triangles(values, bundled):
	if bundled:
		values = transform(values)

	num = sum([is_triange(val) for val in values])
	return num

if __name__ == '__main__':
	with open('input', 'r') as f:
		values = [line.strip('\n').strip() for line in  f.readlines()]

	num = count_triangles(values, bundled=False)
	print num

	num = count_triangles(values, bundled=True)
	print num

