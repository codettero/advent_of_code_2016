import unittest
from day4 import get_sum

class Test_day4(unittest.TestCase):

	def test_get_sum(rooms):
		room_sum = get_sum(['aaaaa-bbb-z-y-x-123[abxyz]',
			'a-b-c-d-e-f-g-h-987[abcde]',
			'not-a-real-room-404[oarel]',
			'totally-real-room-200[decoy]'])
		# self.assertEqual(room_sum, 1514)


if __name__ == '__main__':
	unittest.main()