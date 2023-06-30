from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.views import View
from django.urls import reverse_lazy
    
from .models import Cat, Dog, Owner

url_prefix = 'gview'



# Meta list view
class MyListView(View):
    model = None
    def get(self, request):
        model_name = self.model._meta.model_name.lower()
        template_name = model_name + '_list'
        model_list = get_list_or_404(self.model)
        context = { template_name : model_list, 'model_name' : model_name + 's' }
        return render(request, f'{url_prefix}/{template_name}.html', context)

# Meta details view
class MyDetailsView(View):
    model = None
    def get(self, request, **kwargs):
        for arg in kwargs:
            print(arg)
        
        # Get model name
        model_name = self.model._meta.model_name.lower()
        template_name = model_name + '_details'
        
        # Get context
        model_id = kwargs[model_name + "_id"]
        obj = get_object_or_404(self.model, pk=model_id)
        context = { model_name : obj }
        
        # Render template
        return render(request, f"{url_prefix}/{template_name}.html", context)

class OwnerVoteView(View):
    def post(self, request):
        # extract owner_id
        
        # try to get owner model
        try:
            owner = Owner.objects.get(pk=request.POST['owner'])
        except (KeyError, Owner.DoesNotExist):
            return render(request, 'gview/owner_list.html', {
                "error_message" : "Please select the owner to vote"
            })
        else:
            # Increment score, save changes and redirect back by GET method
            owner.score += 1
            owner.save()
            return HttpResponseRedirect(reverse_lazy('gview:owner_list_url'))

# Meta vote view
class PetVoteView(View):
    pet = None
    def post(self, request, owner_id):
        # Get owner
        owner = get_object_or_404(Owner, pk=owner_id)
        
        # Get pet model name
        model_name = self.model._meta.model_name.lower()
        # Get template name
        template_name = 'owner_details'
        # Get pet id
        pet_id = request.POST[model_name]
        # Get pet object
        
        # Try to get pet object pk from the POST request
        try:
            pet_obj = self.model.objects.get(pk=pet_id)
        # Intercept KeyErrors, when user haven't selected a pet
        except(KeyError, self.model.DoesNotExist):
            # Return user to the form with error message
            return render(request, template_name, {
                'owner': owner,
                'error_message': f"You didn't select a {model_name}"
            })
        else:
            # Increment pet model score
            pet_obj.score += 1
            pet_obj.save()
            
            # Redirect with GET method to acoid POST request repeat
            return HttpResponseRedirect(reverse_lazy('gview:owner_details_url', args=(owner.id,)))

class MyVoteView(View):
    pass



# Custom generic Vote Views
class CatVoteView(PetVoteView):
    model = Cat
class DogVoteView(PetVoteView):
    model = Dog

# Custom generic List Views
class DogListView(MyListView):
    model = Dog
class CatListView(MyListView):
    model = Cat
class OwnerListView(MyListView):
    model = Owner


# Custom generic Details Views
class DogDetailsView(MyDetailsView):
    model = Dog
class CatDetailsView(MyDetailsView):
    model = Cat
class OwnerDetailsView(MyDetailsView):
    model = Owner
    
def about(request):
    context = {}
    return render(request, 'gview/about.html', context)


# Deprecated Views
# class CatListView(View):
#     def get(self, request):
#         cat_list = Cat.objects.order_by('name')
#         context = {'models': cat_list, 'model_name':Cat._meta.model_name}
#         template = loader.get_template('gview/index.html')
#         return HttpResponse(template.render(context, request))


# # auto dog view
# class DogListView(View):
#     def get(self, request):
#         model = Dog
#         model_name = Dog._meta.model_name
#         template_name = model_name.lower() + '_list'
#         context = { 'models' : get_list_or_404(model), 'model_name' : model_name + 's' }
#         return render(request, f'{url_prefix}/{template_name}.html', context)