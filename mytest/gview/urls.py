from django.urls import path
from django.views import generic

from . import views

app_name = 'gview'
urlpatterns = [    
    # Dog and Cat views
    # ListViews
    path('cats/', views.CatListView.as_view(), name='cat_url'),
    path('dogs/', views.DogListView.as_view(), name='dog_view'),
    # DetailViews
    path('dog/<int:dog_id>', views.DogDetailsView.as_view(), name='dog_details_url'),
    path('cat/<int:cat_id>', views.CatDetailsView.as_view(), name='cat_details_url'),
    #VoteViews
    path('owner/<int:owner_id>/cat/vote', views.CatVoteView.as_view(), name='cat_vote_url'),
    path('owner/<int:owner_id>/dog/vote', views.DogVoteView.as_view(), name='dog_vote_url'),
    
    # Owner views
    path('', views.OwnerListView.as_view(), name='owner_list_    url'),
    path('owner/<int:owner_id>', views.OwnerDetailsView.as_view(), name='owner_details_url'),
    path('owner/vote', views.OwnerVoteView.as_view(), name='owner_vote_url'),
    
    # About page 
    path('about/',views.about, name='about_view')
] 