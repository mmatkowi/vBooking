"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.contrib.auth import views as auth_views
from app.forms import BootstrapAuthenticationForm

urlpatterns = [
    path('', views.index, name='index'),
    path('event/', views.event, name='event'),
    path('events/', views.events, name='events'),
    path('reservation/', views.reservation, name='reservation'),
    path('reservations/', views.reservations, name='reservations'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=BootstrapAuthenticationForm), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('posts/', views.posts),
    path('post/', views.post),
    path('admin/', admin.site.urls),
]
