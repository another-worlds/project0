from django.urls import path
from . import views

app_name="myapp"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index_url'),
    path('<int:pk>', views.DetailView.as_view(), name='details_url'),
    path('<int:post_id>/vote', views.vote, name='vote_url'),
    path('about', views.about, name='about_url'),
    path('session', views.sessfun, name='session_url')

]
