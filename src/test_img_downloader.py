import unittest
import sys
import img_downloader
import img_utilities

class TestUrlDownloader(unittest.TestCase):

	def test_url_file_does_not_exist(self):
		filename = './data/urls1.txt'
		img_downloader.read_url_file(filename)				

	def test_get_netloc(self):
		url = 'http://www.mywebserver.com/images/271947.jpg'
		netloc = img_utilities.get_netloc(url)
		self.assertEqual(netloc, 'mywebserver.com')

	def test_get_path(self):
		url = 'http://mywebserver.com/images/271947.jpg'
		path = img_utilities.get_path(url)
		self.assertEqual(path, '/images/271947.jpg')

	def test_get_dirname(self):
		url = 'http://mywebserver.com/images/271947.jpg'
		dirname = img_utilities.get_dirname(url)
		self.assertEqual(dirname, '/images')

	def test_get_basename(self):
		url = 'http://mywebserver.com/images/271947.jpg'
		netloc = img_utilities.get_basename(url)
		self.assertEqual(netloc, '271947.jpg')

	def test_is_valid_img_url(self):
		self.assertTrue(img_utilities.is_valid_img_url('http://mywebserver.com/images/271947.jpg'))
		self.assertTrue(img_utilities.is_valid_img_url('http://mywebserver.com/images/24174.jpg'))
		self.assertFalse(img_utilities.is_valid_img_url('mywebserver.com/images/271947.html'))
		self.assertFalse(img_utilities.is_valid_img_url('http://somewebsrv.com/img/992147.jpg.exe'))

	def test_has_valid_img_ext(self):
		self.assertTrue(img_utilities.has_valid_img_ext('http://mywebserver.com/images/271947.jpg'))
		self.assertTrue(img_utilities.has_valid_img_ext('http://mywebserver.com/271947.bmp'))

if __name__ == "__main__":
	unittest.main()