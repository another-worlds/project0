from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse

# Create your views here.
def myview(request):
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    response = HttpResponse(f'view count={num_visits}    d26e5e36')
    if num_visits >= 3: del(request.session['num_visits'])
    response.set_cookie('dj4e_cookie', 'd26e5e36', max_age=1000)
    return response