from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	# the r is a regular expression that defines which urls it applies to
    # goes on to say where it should send those requests
    # Examples:
    # ^$ means empty string
    url(r'^$', 'lists.views.home_page', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # to 
    url(r'^lists/the-only-list-in-the-world/$','lists.views.view_list', name='view_list'),
    url(r'^lists/new$','lists.views.new_list', name='new_list'),
    #url(r'^admin/', include(admin.site.urls)),
)
