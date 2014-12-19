from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest

from lists.views import home_page
# Create your tests here.

# the tests are run by invoking the Django test runner - a manage.py command.
# $ python3 manage.py test 

class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		# check the response we send from home_page in lists.views starts witg an html tag that is closed
		self.assertTrue(response.content.startswith(b'<html>')) # b is for bytes, have to use to compare
		# check we have a title tag with the words to do in it
		self.assertIn(b'<title>To-Do lists</title>', response.content)
		self.assertTrue(response.content.endswith(b'</html>'))