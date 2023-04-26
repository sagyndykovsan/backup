from django.urls import path
from scholarship import views

urlpatterns = [
    path('', views.scholarship, name="scholarship"),
    path('detail/', views.detail, name="detail"),
    path('', views.scholarship_name, name="scholarship_name"),
    path('detail/<int:pk>/', views.detail, name="detail"),



]