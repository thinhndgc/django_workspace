from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.template import RequestContext
from bookmark.forms import *
# Create your views here.
# @ensure_csrf_cookie


def main_page(request):
    print(request.user.username)
    return render_to_response(
        'main_page.html',
        RequestContext(request)
    )


def user_page(request, username):
    try:
        user = User.objects.get(username=username)
    except:
        raise Http404('Request user not found!')
    bookmarks = user.bookmark_set.all()
    variables = RequestContext(
        request, {
            'username': username,
            'bookmarks': bookmarks
        }
    )
    template = get_template('user_page.html')
    return render_to_response('user_page.html', variables)


def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['user_name'])
            user = User.objects.create_user(
                username=form.cleaned_data['user_name'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/bookmark/register/success/')
    else:
        form = RegistrationForm()

    variables = RequestContext(request, {
        'form': form
    })
    return render_to_response(
        'registration/register.html',
        variables
    )


def log_out(request):
    logout(request)
    return HttpResponseRedirect('/bookmark/login/')
