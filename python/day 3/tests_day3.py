import unittest
from day3 import count_triangles


class Test_Day3(unittest.TestCase):
	def test_count_triangles(self):
		num = count_triangles(['5 10 25', '2 2 4'], bundled=False)
		self.assertEqual(num, 0)

		num = count_triangles(['810  679   10', '783  255  616', '545  626  626',
			'545  626  626', '84  910  149', '607  425  901'], bundled=True)
		self.assertEqual(num, 4)


if __name__ == '__main__':
	unittest.main()