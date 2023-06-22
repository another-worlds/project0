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
    return redirect('details_url', post_id)
def downvote(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        post.score -= 1
        post.save()
    except Post.DoesNotExist:
        raise Http404
    return redirect('details_url', post_id)

def about(request):
    return HttpResponse("""
                        <ul>
                        <li><a href="https://github.com/another-worlds/project0">Github page of the project</a></li>
                        <li><a href="https://docs.google.com/document/d/1d3aU0Vxowz8SOUG6LLcozmLCe--OiDvnVS69Dhko2_U/edit?usp=sharing">To-do list of the project on PythonAnywhere</a></li>
                        </ul>
                        """)