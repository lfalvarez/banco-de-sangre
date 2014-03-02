from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse

# Create your views here.

#home_url = reverse('home')

class UserAccountView(TemplateView):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
    	home_url = reverse('home')
        return super(UserAccountView, self).dispatch(*args, **kwargs)
