from django.shortcuts import render, get_list_or_404, get_object_or_404
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

def details(request, model_id):
    model = get_object_or_404(MyModel, id=model_id)
    submodels = get_list_or_404(MySubmodel, model=model)
    context = {'model': model, 'submodels': submodels}
    
    template = loader.get_template('myapp2/details.html')
    return HttpResponse(template.render(context, request))