from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.QuestionListView.as_view(), name='question_list_url'),
    path('owner', views.owner, name='owner_url'),
    path('<int:pk>', views.QuestionDetailView.as_view(), name='question_detail_url'),
    path('<int:question_id>/vote', views.QuestionVoteView.as_view(), name='question_vote_view')
]
