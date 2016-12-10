import unittest
from day1 import get_HQ_location


class Test_Day1(unittest.TestCase):

	def test_get_length(self):
		length, length_updated = get_HQ_location(['R2', 'L3'])
		self.assertEqual(length, 5)
		length, length_updated = get_HQ_location(['R2', 'R2', 'R2'])
		self.assertEqual(length, 2)
		length, length_updated = get_HQ_location(['R5', 'L5', 'R5', 'R3'])
		self.assertEqual(length, 12)

	def test_get_visited_twice(self):
		length, length_updated = get_HQ_location(['R8', 'R4', 'R4', 'R8'])
		self.assertEqual(length_updated, 4)
		length, length_updated = get_HQ_location(['L3', 'R1', 'R1', 'R3'])
		self.assertEqual(length_updated, 2)


if __name__ == '__main__':
	unittest.main()
