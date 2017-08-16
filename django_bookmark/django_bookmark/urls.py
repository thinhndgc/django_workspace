from django.conf.urls import patterns, include, url
import os.path
from django.contrib import admin
from bookmark.views import *

admin.autodiscover()

static = os.path.join(
    os.path.dirname(__file__), 'static'
)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_bookmark.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^bookmark/$', main_page),
    url(r'^bookmark/user/(\w+)/$', user_page),
    url(r'^bookmark/login/$', 'django.contrib.auth.views.login'),
    url(r'^bookmark/logout/$', log_out),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': static}),
)
