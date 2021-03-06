from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page

from lists.models import Item, List 
# Create your tests here. These are unit tests. Only have one thing for unit tests, 
# i.e. each unit test has one assert block?

# the tests are run by invoking the Django test runner - a manage.py command.
# $ python3 manage.py test 

# these tests shoud be about testing logic, flow control, and configuration. Not really `HTML contstants...
class NewItemTest(TestCase):
	def test_can_save_a_POST_request_to_an_existing_list(self):
		# dont understand this
		other_list = List.objects.create()
		correct_list = List.objects.create()
		self.client.post(
			'/lists/%d/add_item' % (correct_list.id,),
			 data = {'item_text':'A new item for an existing list'}
			)
		self.assertEqual(Item.objects.count(),1)
		new_item = Item.objects.first()
		self.assertEqual(new_item.text, 'A new item for an existing list')
		self.assertEqual(new_item.list, correct_list)

	def test_redirects_to_list_view(self):
		other_list = List.objects.create()
		correct_list = List.objects.create()
		response = self.client.post(
			'/lists/%d/add_item' % (correct_list.id,),
			data = {'item_text':'A new item for an existing list'}
			)
		self.assertRedirects(response, '/lists/%d/' % (correct_list.id,))

class NewListTest(TestCase):

	def test_saving_a_POST_request(self):
		
		self.client.post(
			'/lists/new', # no trailing slash for some reason
			data = {'item_text':'A new list item'}
			)
		self.assertEqual(Item.objects.count(),1)
		new_item = Item.objects.first()
		self.assertEqual(new_item.text, 'A new list item')

		''' without using django tst client
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
		'''
	def test_redirects_after_POST_request(self):
		response = self.client.post(
			'/lists/new',
			data = {'item_text':'A new list item'}
			)
		new_list = List.objects.first()
		self.assertRedirects(response, '/lists/%d/' %(new_list.id,))




		''' without using django tst client
		request = HttpRequest()
		request.method = 'POST'
		request.POST['item_text'] = 'A new list item'

		response = home_page(request)

		# check for redirection after first post request. 
		self.assertEqual(response.status_code, 302, "check for redirection after POST failed: 302 is redirect status code") # reidrect has status code 302
		self.assertEqual(response['location'],'/lists/the-only-list-in-the-world/')
		'''



class ListViewTest(TestCase):
	def test_uses_list_template(self): # as opposed to home template we have been using till now
		list_ = List.objects.create()
		response = self.client.get('/lists/%d/'%(list_.id,))
		self.assertTemplateUsed(response,'list.html') # more django testing method magic!

	def test_displays_all_items(self):
		correct_list = List.objects.create()
		Item.objects.create(text = 'itemey 1',list = correct_list)
		Item.objects.create(text = 'itemey 2',list = correct_list)
		other_list = List.objects.create()
		Item.objects.create(text = 'other list item 1',list = other_list)
		Item.objects.create(text = 'other list item 2',list = other_list)
		# response is no longer a got through sending request to homepage.
		response = self.client.get('/lists/%d/'%(correct_list.id,))

		self.assertContains(response,'itemey 1')# the Django assertContains method knows how to deal with responses and the bytes of their content.
		self.assertContains(response,'itemey 2')
		self.assertNotContains(response,'other list item 1')
		self.assertNotContains(response,'other list item 2')

	def test_passes_correct_list_to_template(self):
		other_list = List.objects.create()
		correct_list = List.objects.create()
		response = self.client.get('/lists/%d/' % (correct_list.id,))
		self.assertEqual(response.context['list'], correct_list)


class ListAndItemModelTest(TestCase):
	def test_saving_and_retrieving_items(self):
		list_ = List()
		list_.save()

		first_item = Item()
		first_item.text = 'The first (ever) list item'
		first_item.list = list_ 
		first_item.save()

		second_item = Item()
		second_item.text = 'Second list item'
		second_item.list = list_
		second_item.save()

		saved_list = List.objects.first()
		self.assertEqual(saved_list, list_) # check that the id is the same

		saved_items = Item.objects.all() # returns a list? - actually a QuerySet
		self.assertEqual(saved_items.count(),2)

		first_saved_item = saved_items[0]
		second_saved_item = saved_items[1]
		self.assertEqual(first_saved_item.text , 'The first (ever) list item')
		self.assertEqual(first_saved_item.list , list_)
		self.assertEqual(second_saved_item.text , 'Second list item')
		self.assertEqual(second_saved_item.list , list_)


class HomePageTest(TestCase):

	# this used to have a test for checking that it displayed all the items, but
	# as it now is only going to contain an empty box, no longer needed. 
	# class ListViewTest now does this

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

	
		'''

		self.assertIn('A new list item', response.content.decode())
		expected_html = render_to_string(
			'home.html',
			{'new_item_text': 'A new list item'})
		self.assertEqual(response.content.decode(),expected_html)
		'''
		