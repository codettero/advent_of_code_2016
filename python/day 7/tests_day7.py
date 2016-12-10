import unittest
from day7 import supports_TLS, count_IPs, has_ABBA, supports_SSL

class Test_day7(unittest.TestCase):

	def test_supports_TLS(self):
		self.assertTrue(supports_TLS('abba[mnop]qrst'))
		self.assertFalse(supports_TLS('abcd[bddb]xyyx'))
		self.assertFalse(supports_TLS('aaaa[qwer]tyui'))
		self.assertTrue(supports_TLS('ioxxoj[asdfgh]zxcvbn'))

	def test_count_TLS_IPs(self):
		self.assertEqual(count_IPs(['abba[mnop]qrst', 
			'abcd[bddb]xyyx',
			'aaaa[qwer]tyui',
			'ioxxoj[asdfgh]zxcvbn'], supports='TLS'), 2)

	def test_is_mirrored(self):
		self.assertTrue(has_ABBA('abba'))
		self.assertFalse(has_ABBA('xxxxxx'))
		self.assertTrue(has_ABBA('cddttddt'))

	def test_supports_SSL(self):
		self.assertTrue(supports_SSL('aba[bab]xyz'))
		self.assertFalse(supports_SSL('xyx[xyx]xyx'))
		self.assertTrue(supports_SSL('aaa[kek]eke'))
		self.assertTrue(supports_SSL('zazbz[bzb]cdb'))

	def test_SSL_IPs(self):
		self.assertEqual(count_IPs(['aba[bab]xyz',
			'xyx[xyx]xy',
			'aaa[kek]eke',
			'zazbz[bzb]cdb'], supports='SSL'), 3)

if __name__ == '__main__':
	unittest.main()