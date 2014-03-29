from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, CreateView
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

class AppointmentCreateView(CreateView):
	form_class = AppointmentModelForm
	template_name = "sangre/your-profile.html"

	def get_form_kwargs(self):
		kwargs = super(AppointmentCreateView, self).get_form_kwargs()
		kwargs['donor'] = self.request.user
		return kwargs

	def get_success_url(self):
		return reverse('account')