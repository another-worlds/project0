from django.urls import path

from . import views


app_name = 'hello'
urlpatterns = [
    path('', views.myview, name='index_url'),
    path('test', views.a_view, name='test_utl')
]
