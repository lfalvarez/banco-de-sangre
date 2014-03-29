from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from dona_sangre.views import UserAccountView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="sangre/home.html"), name="home"),
    url(r'^create_appointment/?$', TemplateView.as_view(template_name="sangre/home.html"), name="create_appointment"),
    url(r'^account/?$', UserAccountView.as_view(), name="account"),
    url(r'^accounts/logout/$','django.contrib.auth.views.logout_then_login', name="logout"),
)