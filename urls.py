from django.urls import path
from . import views

urlpatterns = [
   # path('', views.home, name='blog-home'),
    path('landing/', views.landing, name='landing')
]