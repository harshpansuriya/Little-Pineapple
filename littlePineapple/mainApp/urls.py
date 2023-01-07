from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.home),
    path('about/', views.about, name="about"),
    path('menu/', views.about, name="menu"),
    path('book/', views.about, name="book"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('addskill/', views.addSkill, name="addskill"),
    path('register/', views.register, name="register")
]
