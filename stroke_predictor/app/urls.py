from django.urls import path, include
from . import views

app_name = "app"
urlpatterns = [
    path('home/', views.home,  name="home"),
    path('form/', views.form,  name="form"),
    path('result/', views.result,  name="result"),
    path('api/stroke/', views.stroke,  name="stroke"),
    path('api/no_stroke/', views.no_stroke,  name="no_stroke"),
    path('api/filter/', views.filter,  name="filter"),
]