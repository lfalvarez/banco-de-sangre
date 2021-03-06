from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, CreateView, DetailView
from django.core.urlresolvers import reverse
from dona_sangre.forms import AppointmentModelForm
from dona_sangre.models import Appointment, FacebookDonor
from django.shortcuts import get_object_or_404

# Create your views here.

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

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        
        return super(AppointmentCreateView, self).dispatch(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(AppointmentCreateView, self).get_form_kwargs()
        kwargs['donor'] = self.request.user
        return kwargs

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(new_appointment_form=form))

class AppointmentDetailView(DetailView):
    model = Appointment
    template_name = 'sangre/appointment.html'

    def get_queryset(self):
        donor = get_object_or_404(FacebookDonor, id=self.request.user.id)
        return Appointment.objects.filter(donor=donor)