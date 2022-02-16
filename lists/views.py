from django.http import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return render(request, 'lists/home.html')
