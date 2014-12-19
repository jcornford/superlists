from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	# the r is a regular expression that defines which urls it applies to
    # goes on to say where it should send those requests
    # Examples:
    # ^$ means empty string
    url(r'^$', 'lists.views.home_page', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
)
