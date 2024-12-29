from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from functools import wraps

def subscription_required(view_func):
    @wraps(view_func)
    @login_required
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.profile.is_subscribed or request.user.profile.is_trial:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('subscriptions')
        else:
            return redirect('login')
    return _wrapped_view

def verified_required(view_func):
    @wraps(view_func)
    @login_required
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.profile.is_verified:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('home')
        else:
            return redirect('login')
    return _wrapped_view