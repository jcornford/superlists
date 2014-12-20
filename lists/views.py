from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
	return render(request, 'home.html', {
		'new_item_text' : request.POST.get('item_text','') #the method get() returns a value for the given key. If key is not available then returns default value None.
		})
