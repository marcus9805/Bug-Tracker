from django.contrib.auth import views as auth_views
from django.urls import path 

from . import views
from .forms import LoginForm
from .views import sign_out

app_name = 'core' 

urlpatterns = [ 
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('signout/', views.sign_out, name='signout'),
]