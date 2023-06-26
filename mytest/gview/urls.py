from django.urls import path

from . import views

app_name = 'gview'
urlpatterns = [
    path('cats/', views.CatListView.as_view(), name='index_url'),
    path('dogs/', views.DogListView.as_view(), name='dog_view'),
    path('<int:dog_id>', views.DogDetailsView.as_view(), name='dog_details_url'),
    path('<int:cat_id>', views.CatDetailsView.as_view(), name='cat_details_url'),
    path('about/',views.about, name='about_view')
] 