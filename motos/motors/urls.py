from django.urls import path
from . import views as vw_mtr
from django.contrib.auth import views as vw_auth
from .forms import LoginForm

app_name ='motors'

urlpatterns = [
    path('', vw_mtr.index, name='index'),
    path('contact/', vw_mtr.contact, name='contact'),
    path('singup/', vw_mtr.singup, name='singup'),
    path('login/', vw_auth.LoginView.as_view(template_name='motors/login.html', authentication_form=LoginForm), name='login')
]