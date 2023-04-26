from django.urls import path
from fond_app import views

urlpatterns = [
    path('', views.index, name="index"),
    path('presentation/', views.presentation, name="presentation"),
    
    path('book/', views.book, name="book"),
    path('video/', views.video, name="video"),
    path('news/', views.news, name="news"),

]