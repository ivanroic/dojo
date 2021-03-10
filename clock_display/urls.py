from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('clock_display', views.index),
]