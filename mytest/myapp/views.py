from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.views import View, generic
from django.urls import reverse, reverse_lazy

from .models import Post, Comment

# Temporary helper function for handling untemplated responses

# View selected post and it's comments
class IndexView(generic.ListView):
    model = Post
    template_name = 'myapp/index.html'
    #context_object_name = 'posts'
    
    def get_queryset(self):
        return Post.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Post
    template_name= 'myapp/details.html'
    
def sessfun(request):
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    if num_visits >= 4: del(request.session['num_visits'])
    return HttpResponse("view_count: " + str(num_visits))

def vote(request, post_id):
    # Get Post id from GET
    post = get_object_or_404(Post, pk=post_id)
    # Get Comment id from POST
    try:
        comment = Comment.objects.get(pk=request.POST['comment'])
    # Send error if no comment selected
    except (KeyError, Comment.DoesNotExist):
        return render(request, 'myapp/details.html', {
            "post": post,
            "error_message" : "ERROR: comment not selected."
        })
    # Increment score if comment found  
    else:
        comment.score += 1
        comment.save()
    # Redirect with GET method
    return HttpResponseRedirect(reverse_lazy('myapp:details_url', args=(post.id,)))

def about(request):
    template = loader.get_template('myapp/about.html')
    context= {}
    return HttpResponse(template.render(context, request))
