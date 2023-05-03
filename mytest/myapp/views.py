from django.shortcuts import render
from django.http import HttpResponse

from .models import Post, Comment

# Create your views here.
def index(request):
    posts = Post.objects.order_by('-pub_date')[5]
    return HttpResponse("")