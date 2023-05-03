from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Post, Comment

# Temporary helper function for handling untemplated responses
def view_item(score, title, tag="h3"):
    return f"<{tag}>{score} | {title}</{tag}>"


# View 5 latest posts 
def index(request):
    posts = Post.objects.order_by('-pub_date')[:5]
    result = []
    for i in range(len(posts)):
        result.append(view_item(posts[i].score, posts[i].title))
    "<br>".join(result)
    return HttpResponse(result)

# View selected post and it's comments
def details(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        comments = post.comment_set.all()
        result = []
        result.append(view_item(post.score, post.title))
        if comments:
            for comment in comments:
                result.append(view_item(comment.score, comment.author, tag='h4'))
        else:
            result.append("Post wasn't commented yet")
    except Post.DoesNotExist:
        raise Http404
    "<br>".join(result)
    return HttpResponse(result)