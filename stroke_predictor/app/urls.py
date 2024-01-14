from django.urls import path, include
from . import views

app_name = "app"
urlpatterns = [
    path('home/', views.home,  name="home"),
    path('form/', views.form,  name="form"),
    path('result/', views.result,  name="result"),
]