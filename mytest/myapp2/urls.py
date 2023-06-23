from django.urls import path
from . import views


app_name = 'myapp2'
urlpatterns = [
    path('', views.index, name='index_url'),
    path('<int:model_id>', views.details, name='details_url')
]
