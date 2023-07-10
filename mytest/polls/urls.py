from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.QuestionListView.as_view(), name='question_list_url'),
    path('owner', views.owner, name='owner_url'),
    path('<int:pk>', views.QuestionDetailView.as_view(), name='question_detail_url'),
    path('<int:question_id>/vote', views.QuestionVoteView.as_view(), name='question_vote_view'),
    path('<int:pk>/results', views.ResultsView.as_view(), name='results_url'),
    path('about/', views.about, name='about_url')
]