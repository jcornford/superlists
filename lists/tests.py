from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page
# Create your tests here.

# the tests are run by invoking the Django test runner - a manage.py command.
# $ python3 manage.py test 

class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)