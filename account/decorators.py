from django.http import HttpResponse
from django.shortcuts import redirect

def authdUser(view_func):
    def wrapper_func(request, *args, **kwargs):
        return view_func(request, *args, **kwargs)
    return wrapper_func


def allowedUser(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("Kamu tidak ter-otorisasi bro!, kami rekam jejak anda.")

        return wrapper_func
    return decorator
