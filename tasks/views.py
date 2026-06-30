from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home (requst):
    return HttpResponse('<h1> welcome to madam glory\'s kitchen</h1>')

def about (request):
    return HttpResponse('<h1> my first code\'s</h1>')

def contact (request):
    return HttpResponse('<h1> my contact\'s</h1>')
