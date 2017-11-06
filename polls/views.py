from django.shortcuts import render
from django.http import HttpResponse

# Create function index that takes in a request
# To call a view we must map it to a URL. Check 'urls.py'
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")