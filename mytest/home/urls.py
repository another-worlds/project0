from django.urls import path
from django.views import generic

from . import views

urlpatterns = [
    path('', views.myview, name='myview_url')
]