import unittest
import sys
import img_downloader
import img_utilities

class TestUrlDownloader(unittest.TestCase):
				print("================Executing Test Cases=====================")
				
				def test_url_file_does_not_exist(self):
								print("Executing test_url_file_does_not_exist==>")
								filename = './data/urls1.txt'
								img_downloader.read_url_file(filename)

				def test_is_valid_img_url(self):
					print("Executing test_is_valid_img_url==>")
					self.assertTrue(img_utilities.is_valid_img_url('http://mywebserver.com/images/271947.jpg'))
					self.assertTrue(img_utilities.is_valid_img_url('http://mywebserver.com/images/24174.jpg'))
					self.assertTrue(img_utilities.is_valid_img_url('http://somewebsrv.com/img/992147.jpg'))
					self.assertFalse(img_utilities.is_valid_img_url('mywebserver.com/images/271947.jpg'))
					self.assertFalse(img_utilities.is_valid_img_url('mywebserver.com/images/271947.html'))
					self.assertFalse(img_utilities.is_valid_img_url('http://somewebsrv.com/img/992147.jpg.exe'))

				def test_has_valid_img_ext(self):
					print("Executing test_has_valid_img_ext==>")
					self.assertTrue(img_utilities.has_valid_img_ext('http://mywebserver.com/images/271947.jpg'))
					self.assertTrue(img_utilities.has_valid_img_ext('http://mywebserver.com/271947.bmp'))

if __name__ == "__main__":
				unittest.main()