from django.urls import path
from news import views

urlpatterns = [
    path('', views.news, name="news"),
    path('detail_news/', views.detail_news, name="detail_news"),
]