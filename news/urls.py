from django.urls import path
from news import views

urlpatterns = [

    path('', views.news, name="news"),
    # path('detail/', views.detail, name="detail"),

]