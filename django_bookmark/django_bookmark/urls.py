import os.path
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
from bookmark.views import *

admin.autodiscover()

static = os.path.join(
    os.path.dirname(__file__), 'static'
)

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_bookmark.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^bookmark/$', main_page),
    url(r'^bookmark/user/(\w+)/$', user_page),
    url(r'^bookmark/login/$', 'django.contrib.auth.views.login'),
    url(r'^bookmark/logout/$', log_out),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': static}),
    url(r'^bookmark/register/$', register_page),
    url(r'^bookmark/register/success/$', TemplateView.as_view(template_name='registration/register_success.html'), name = "regiser_success")
]
