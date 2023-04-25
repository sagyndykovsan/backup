from django.urls import path
from scholarship import views

urlpatterns = [

    path('', views.scholarship, name="scholarship"),
    path('detail/', views.detail, name="detail"),

]