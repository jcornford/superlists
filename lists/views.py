from django.shortcuts import redirect, render
from django.http import HttpResponse

from lists.models import Item

# Create your views here.
def home_page(request):
	if request.method == 'POST':
		new_item_text = request.POST['item_text']
		Item.objects.create(text=new_item_text) # this saves the item
		return redirect('/')

	items = Item.objects.all() # used so can be added to the return render
	return render(request, 'home.html', {'items':items})
