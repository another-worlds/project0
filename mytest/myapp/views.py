from django.shortcuts import render
from django.http import HttpResponse

from .models import Post, Comment

# Create your views here.
def index(request):
    posts = Post.objects.order_by('-pub_date')[:5]
    result = []
    for i in range(len(posts)):
        result.append(f"<h3>{posts[i].score} | {posts[i].title}<h3>")
    "<br>".join(result)
    return HttpResponse(result)