from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='Home'),
    path('generate',views.generate,name='Home'),
    path('display-image', views.display_image, name='display_image'),

]
