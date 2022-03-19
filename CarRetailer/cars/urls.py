from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home-car'),
    path("<slug:slug>/",views.models,name="home-model"),
]
