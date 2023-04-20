from django.urls import path
from fond_app import views

urlpatterns = [
    path('', views.index, name="index"),
]