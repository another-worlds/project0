from django.shortcuts import render
from django.template import loader

from django.http import HttpResponse, Http404

from .models import MyModel, MySubmodel


# Create your views here.
def index(request):
    try:
        posts = MyModel.objects.all()
    except MyModel.DoesNotExist:
        return Http404
    context = {"posts":posts}
    
    template = loader.get_template('myapp2/index.html')
    return HttpResponse(template.render(context, request))
    