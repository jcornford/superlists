from django.test import TestCase

# Create your tests here.

# the tests are run by invoking the Django test runner - a manage.py command.
# $ python3 manage.py test 

class SmokeTest(TestCase):

	def test_bad_maths(self):
		self.assertEqual(1+1,3)