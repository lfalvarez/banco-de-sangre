from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from dona_sangre.forms import AppointmentModelForm

# Create your views here.

#home_url = reverse('home')

class UserAccountView(TemplateView):
    template_name = "sangre/your-profile.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        home_url = reverse('home')
        return super(UserAccountView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UserAccountView, self).get_context_data(**kwargs)
        context['new_appointment_form'] = AppointmentModelForm()
        return context
