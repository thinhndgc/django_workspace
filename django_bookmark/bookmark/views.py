from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.decorators import login_required
# Create your views here.
# @ensure_csrf_cookie
# @login_required(login_url='/bookmark/login/')
def main_page(request):
    print(request.user.username)
    return render_to_response(
        'main_page.html',
        {'user': request.user}
    )

def user_page(request, username):
    try:
        user = User.objects.get(username=username)
    except:
        raise Http404('Request user not found!')
    bookmarks = user.bookmark_set.all()
    template = get_template('user_page.html')
    variables = Context(
        {
            'username': username,
            'bookmarks': bookmarks
        }
    )
    output = template.render(variables)
    return HttpResponse(output)