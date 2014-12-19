from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page
# Create your tests here. These are unit tests

# the tests are run by invoking the Django test runner - a manage.py command.
# $ python3 manage.py test 

# these tests shoud be about testing logic, flow control, and configuration. Not really `HTML contstants...

class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		# check the response we send from home_page in lists.views starts witg an html tag that is closed
		expected_html = render_to_string('home.html')
		self.assertEqual(response.content.decode(), expected_html)
		#use decode() to convert the respinse.content bytes int a python unicode string.