from django.conf.urls import patterns, url



# just lists
	#BEWARE GREEDY REGULAR EXPRESSIONS AND 301 error: permemant redirect. Almost right, except for missing /
	# fixed with \d in regualr expression to select only for numerical digits.
	# the r is a regular expression that defines which urls it applies to
    # goes on to say where it should send those requests
    # Examples:
    # ^$ means empty string

    
urlpatterns = patterns('',
    url(r'^(\d+)/$', 'lists.views.view_list', name='view_list'),
    url(r'^(\d+)/add_item$', 'lists.views.add_item', name='add_item'),
    url(r'^new$', 'lists.views.new_list', name='new_list'),
    
              
)