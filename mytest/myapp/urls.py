from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_url'),
    path('<int:post_id>', views.details, name='details_url')
]
