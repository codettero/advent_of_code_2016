import unittest
from day6 import get_message

class Test_day6(unittest.TestCase):

	def test_get_message(self):
		signals = ['eedadn', 'drvtee', 'eandsr', 'raavrd', 'atevrs','tsrnev',
		'sdttsa', 'rasrtv', 'nssdts', 'ntnada', 'svetve', 'tesnvt', 'vntsnd',
		'vrdear', 'dvrsen', 'enarar']
		message = get_message(signals, 'max')
		self.assertEqual(message, 'easter')
		message = get_message(signals, 'min')
		self.assertEqual(message, 'advent')


if __name__ == '__main__':
	unittest.main()