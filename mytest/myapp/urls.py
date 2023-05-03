from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_url'),
    path('<int:post_id>', views.details, name='details_url'),
    path('about', views.about, name='about_url'),
    path('<int:post_id>/upvote', views.upvote, name='upvote_url'),
    path('<int:post_id>/downvote', views.downvote, name='downvote_url')
]
