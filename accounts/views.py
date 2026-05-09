from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'


class CustomLogoutView(LogoutView):
    pass