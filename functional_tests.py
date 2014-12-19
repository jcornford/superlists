from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
	    self.browser = webdriver.Firefox()
	    self.browser.implicitly_wait(3) #to make sure selenium waits for pages to complete loading

	def tearDown(self):
		self.browser.quit()

	def testMakelist(self):
		#User checks out the webpage
		self.browser.get('http://localhost:8000')

		#user notices that page title and header mention to-do lists
		self.assertIn('To-Do',self.browser.title) 
		self.fail('Finish the test!')


		#she is invited to enter a to-do item straight away

		#she types buy slippers

		#she hits enter, the page updates, and now page lists buy peakcock feathers

		#still a text box inviting her to add a another item

		#page udates and npw shows both items

		#user wonders whether the page will remeber her list, she then sees that the 
		#site has generated a unqiue earl for her -- there is some text

		#she visits that url, her to do list is still there

		#she fucks off

if __name__ =='__main__':
	#call unittest.main(), which launches the unittest test runner, which finds test
	#classes and methods ijn the file and runs them.
	unittest.main(warnings='ignore')



