from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Post, Comment

# Temporary helper function for handling untemplated responses
def view_item(score, title, tag="h3"):
    return f"<{tag}>{score} | {title}</{tag}>"


# View 5 latest posts 
def index(request):
    posts = Post.objects.order_by('-pub_date')[:5]
    context = { 'posts' : posts }
    template = loader.get_template('myapp/index.html')
    return HttpResponse(template.render(context, request))

# View selected post and it's comments
def details(request, post_id):
    template = loader.get_template('myapp/details.html')
    
    try:
        post = Post.objects.get(id=post_id)
        comments = post.comment_set.order_by('score')
    except Post.DoesNotExist:
        raise Http404
    context = {'post': post, 'comments': comments}
    return HttpResponse(template.render(context, request))

def upvote(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        post.score += 1
        post.save()
    except Post.DoesNotExist:
        raise Http404
    return redirect('myapp:details_url', post_id)
def downvote(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        post.score -= 1
        post.save()
    except Post.DoesNotExist:
        raise Http404
    return redirect('myapp:details_url', post_id)

def about(request):
    template = loader.get_template('myapp/about.html')
    context= {}
    return HttpResponse(template.render(context, request))