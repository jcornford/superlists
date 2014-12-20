from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import unittest

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
	    self.browser = webdriver.Firefox()
	    self.browser.implicitly_wait(3) #to make sure selenium waits for pages to complete loading

	def tearDown(self):
		self.browser.quit()

	def check_for_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows  = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])

	def test_can_start_a_list_and_retrieve_it_later(self):
		#User checks out the webpage
		self.browser.get('http://localhost:8000')

		#user notices that page title AND header mention to-do lists
		self.assertIn('To-Do',self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do',header_text)

		#she is invited to enter a to-do item straight away
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
			)

		#she types buy slippers
		inputbox.send_keys('Buy slippers')

		#she hits enter, the page updates, and now page lists buy peakcock feathers
		inputbox.send_keys(Keys.ENTER)

		check_for_row_in_list_table('1: Buy slippers')

		#still a text box inviting her to add a another item
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Put on slippers')
		inputbox.send_keys(Keys.ENTER)

		#page udates and npw shows both items
		check_for_row_in_list_table('1: Buy slippers')
		check_for_row_in_list_table('2: Put on slippers')

		#user wonders whether the page will remeber her list, she then sees that the 
		#site has generated a unqiue earl for her -- there is some text

		#she visits that url, her to do list is still there

		#she fucks off

		self.fail('Finish the functional fucking test!')


		

		

if __name__ =='__main__':
	#call unittest.main(), which launches the unittest test runner, which finds test
	#classes and methods ijn the file and runs them.
	unittest.main(warnings='ignore')



