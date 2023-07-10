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

def a_view(request):
    # increment or cretae "num_requests" variable
    num_requests = request.session.get('num_requests', 0) + 1
    
    # save changes to the variable
    request.session['num_requests'] = num_requests
    
    # if num requests > 4: delete cookie
    if num_requests >=4: del(request.session['num_requests'])
    
    # generate response
    response  = HttpResponse(f"num requests: {num_requests}")
    
    # set arbitraty cookie
    response.set_cookie("my_cookie", "1337", max_age=1000)
    
    return response