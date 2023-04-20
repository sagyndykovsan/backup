from django.urls import path
from scholarship import views

urlpatterns = [
    path('', views.index, name="index"),
]