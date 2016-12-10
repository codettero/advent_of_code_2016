class Node(object):
	def __init__(self, trans, left=None, right=None):
		self.right = right
		self.left = left
		self.trans = trans

class LinkedList(object):
	def __init__(self):
		self._elems = []
		self.current = None

	def add(self, node):
		if not self._elems:
			node.left = node
			node.right = node
			self.current = node
		else:
			node.left = self._elems[-1]
			self._elems[-1].right = node
			node.right = self._elems[0]
			self._elems[0].left = node

		self._elems.append(node)

	def turn_left(self):
		self.current = self.current.left
		return self.current

	def turn_right(self):
		self.current = self.current.right
		return self.current

def _create_orientations():
	orientation = LinkedList()
	orientation.add(Node(lambda x, y, val: (x, y+val)))
	orientation.add(Node(lambda x, y, val: (x+val, y)))
	orientation.add(Node(lambda x, y, val: (x, y-val)))
	orientation.add(Node(lambda x, y, val: (x-val, y)))

	return orientation

def _get_orientation(direction, orientation):
	if direction == 'L':
		return orientation.turn_left()
	else:
		return orientation.turn_right()

def get_HQ_location(instructions):
	visited = []
	visited_twice = None
	x, y = (0, 0)
	orientation = _create_orientations()

	for instr in instructions:
		new_coords = _get_orientation(instr[0], orientation).trans(x, y, int(instr[1:]))
		
		if not visited_twice and x == new_coords[0]:
			for coord in [(x, c) for c in range(min(y, new_coords[1]), max(y, new_coords[1])) if (x, c) != new_coords]:
				if coord in visited:
					visited_twice = coord
					break
				else:
					visited.append(coord)
		elif not visited_twice and y == new_coords[1]:
			for coord in [(c, y) for c in range(min(x, new_coords[0]), max(x, new_coords[0])) if (c, y) != new_coords]:
				if coord in visited:
					visited_twice = coord
					break
				else:
					visited.append(coord)

		x, y = new_coords

	length = abs(x) + abs(y)
	length_updated = abs(visited_twice[0]) + abs(visited_twice[1]) if visited_twice else 0
	return length, length_updated


if __name__ == '__main__':
	with open('input', 'r') as f:
		instructions = [i.strip(',') for i in f.read().split()]

		length, length_updated = get_HQ_location(instructions)
		print length
		print length_updated
