from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse

# Create your views here.
def myview(request):
    response = HttpResponse('d26e5e36')
    response.set_cookie('dj4e_cookie', 'd26e5e36', max_age=1000)
    return response