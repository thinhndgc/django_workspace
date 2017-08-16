from django.conf.urls import patterns, include, url

from django.contrib import admin
from bookmark.views import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_bookmark.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^bookmark/$', main_page),
    url(r'^bookmark/user/(\w+)/$', user_page),
    url(r'^bookmark/login/$', 'django.contrib.auth.views.login'),
    url(r'^bookmark/logout/$', log_out),    
)
