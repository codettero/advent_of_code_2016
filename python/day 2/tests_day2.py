import unittest
from day2 import get_code

class Test_Day2(unittest.TestCase):

	def test_get_code(self):
		code = get_code((1, 1), ['ULL', 'RRDDD', 'LURDL', 'UUUUD'], new=False)
		self.assertEqual(code, '1985')
		code = get_code((1, -1), ['ULL', 'RRDDD', 'LURDL', 'UUUUD'], new=True)
		self.assertEqual(code, '5DB3')

if __name__ == '__main__':
	unittest.main()