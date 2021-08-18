from student import admin
from django.urls.base import reverse
from django.http.response import HttpResponse, HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin


class LoginCheckMiddleware(MiddlewareMixin):
    def process_view(self,request,view_func,view_args,view_kwargs):
        modulename=view_func.__module__
        user=request.user
        if user.is_authenticated:
            pass
        else:
            if request.path == reverse('show-student') or request.path == "/login/" or request.path == '/dologin/' or request.path == '/search-url' :
                pass
            else:
                print(request.path)
                return HttpResponse('Method not Allowed...')
