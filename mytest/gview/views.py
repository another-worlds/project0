from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from django.views import View
    
from .models import Cat, Dog

url_prefix = 'gview'

# default cat view
class CatListView(View):
    def get(self, request):
        cat_list = Cat.objects.order_by('name')
        context = {'models': cat_list, 'model_name':Cat._meta.model_name}
        template = loader.get_template('gview/index.html')
        return HttpResponse(template.render(context, request))


# auto dog view
class DogListView(View):
    def get(self, request):
        model = Dog
        model_name = Dog._meta.model_name
        template_name = model_name.lower() + '_list'
        context = { 'models' : get_list_or_404(model), 'model_name' : model_name + 's' }
        return render(request, f'{url_prefix}/{template_name}.html', context)

# meta class prototype
class MyListView(View):
    model = None
    def get(self, request):
        model_name = self.model._meta.model_name
        template_name = model_name.lower() + '_list'
        model_list = get_list_or_404(self.model)
        context = { template_name : model_list, 'model_name' : model_name + 's' }
        return render(request, f'{url_prefix}/{template_name}.html', context)

# inherited class view
class DogListView(MyListView):
    model = Dog

class DogDetailsView(View):
    def get(self, request, dog_id):
        return HttpResponse('Dog details')

class CatDetailsView(View):
    def get(self, request, cat_id):
        return HttpResponse('Cat details')

def about(request):
    context = {}
    return render(request, 'gview/about.html', context)