from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page

from lists.models import Item
# Create your tests here. These are unit tests

# the tests are run by invoking the Django test runner - a manage.py command.
# $ python3 manage.py test 

# these tests shoud be about testing logic, flow control, and configuration. Not really `HTML contstants...


class ItemModelTest(TestCase):
	def test_saving_and_retrieving_items(self):

		first_item = Item()
		first_item.text = 'The first (ever) list item'
		first_item.save()

		second_item = Item()
		second_item.text = 'Second list item'
		second_item.save()

		saved_items = Item.objects.all() # returns a list? - actually a QuerySet
		self.assertEqual(saved_items.count(),2)

		first_saved_item = saved_items[0]
		second_saved_item = saved_items[1]
		self.assertEqual(first_saved_item.text , 'The first (ever) list item')
		self.assertEqual(second_saved_item.text , 'Second list item')


class HomePageTest(TestCase):

	def test_home_page_only_saves_items_when_necessary(self):
		request = HttpRequest()
		home_page(request) # this is not sending a POST method to views.home_page, so should not save anything
		self.assertEqual(Item.objects.count(),0)

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

	def test_home_page_can_save_a_POST_request(self):
		# setup 
		request = HttpRequest()
		request.method = 'POST'
		request.POST['item_text'] = 'A new list item'

		# exercise 
		response = home_page(request)

		#assert
		# to check that view saves a new item, not just passing it through to its response
		self.assertEqual(Item.objects.count(),1)
		new_item = Item.objects.first() # this is the same as objects.all()[0]
		self.assertEqual(new_item.text,'A new list item')

		self.assertIn('A new list item', response.content.decode())
		expected_html = render_to_string(
			'home.html',
			{'new_item_text': 'A new list item'})
		self.assertEqual(response.content.decode(),expected_html)
		