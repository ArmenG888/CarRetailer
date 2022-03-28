from django.urls import path
from . import views
urlpatterns = [
    path("", views.home,name="car-home"),
    path('brands/', views.brands, name='brand'),
    path("<slug:slug>/",views.DetailView.as_view(),name="home-model"),
]
