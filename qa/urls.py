from django.urls import path
from qa import views

urlpatterns = [
    path('', views.qa, name="qa"),
]