from django.shortcuts import render

# Create your views here.
def home_page(request):

	return render (request, 'home.html') # django automatically searches folders called templates inside you apps' directories
