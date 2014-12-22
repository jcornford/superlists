from django.conf.urls import patterns, include, url
from django.contrib import admin


	#BEWARE GREEDY REGULAR EXPRESSIONS AND 301 error: permemant redirect. Almost right, except for missing /
	# fixed with \d in regualr expression to select only for numerical digits.
	# the r is a regular expression that defines which urls it applies to
    # goes on to say where it should send those requests
    # Examples:
    # ^$ means empty string


urlpatterns = patterns('',
    url(r'^$', 'lists.views.home_page', name='home'),
    url(r'^lists/',include('lists.urls')), # to make ists self contained
    url(r'^lists/new$', 'lists.views.new_list', name='new_list'),
    # url(r'^admin/', include(admin.site.urls)),
)
