from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views import View, generic
from django.urls import reverse_lazy

from .models import Question, Choice

def owner(request):
    return HttpResponse("Hello, world. d26e5e36 is the polls owner.d26e5e36")


class QuestionListView(generic.ListView):
    model = Question
    
class QuestionDetailView(generic.DetailView):
    model = Question

class QuestionVoteView(View):
    def post(self, request, question_id):
        # get question
        question = get_object_or_404(Question, pk=question_id)
        
        # get choice or return error message
        try:
            choice = Choice.objects.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            return render(request, 'polls/question_detail.html', {
                "question" : question,
                "error_message": "Please select a choice"
            })
        else:
            choice.votes += 1
            choice.save()
            return HttpResponseRedirect(reverse_lazy('polls:question_detail_url', args=(question.id,)))