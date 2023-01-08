from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'skills', views.SkillViewSet, 'skills')

urlpatterns = [
    path('', views.home),
    path('about/', views.about, name="about"),
    path('menu/', views.about, name="menu"),
    path('book/', views.about, name="book"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('addskill/', views.addSkill, name="addskill"),
    path('register/', views.register, name="register"),

    path('api/', include(router.urls)),
]
