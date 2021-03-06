from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from dona_sangre.views import UserAccountView, AppointmentCreateView, AppointmentDetailView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="sangre/home.html"), name="home"),
    url(r'^create_appointment/?$', AppointmentCreateView.as_view(), name="create_appointment"),
    url(r'^appointment/(?P<pk>[-\d]+)/?$', AppointmentDetailView.as_view(), name="appointment_detail"),
    url(r'^account/?$', UserAccountView.as_view(), name="account"),
    url(r'^accounts/logout/$','django.contrib.auth.views.logout_then_login', name="logout"),
)