from django.http import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return HttpResponse('<!DOCTYPE html><title>To-Do lists</title></html>')
