from django.conf.urls import url,include
from django.contrib import admin
from app01 import  views
urlpatterns = [

    url(r'^user/', views.UserView.as_view()),
]
