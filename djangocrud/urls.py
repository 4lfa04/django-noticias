"""
URL configuration for djangocrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls import handler404
from noticias import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.signin, name='login'),
    path('signout/', views.signout, name='login'),
    path('getNotices/', views.noticias, name='getNotices'),
    path('user_dash/', views.user_dash, name='user_dash'),
    path('crear_noticia/', views.crear_noticia, name='crear_noticia'),
    path('mis_noticias/', views.mis_noticias_view, name='mis_noticias'),
    path('noticia/<int:noticia_id>/', views.user_noticia, name='noticia'),
]