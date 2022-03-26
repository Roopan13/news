from email.mime import image
from turtle import title
from django.shortcuts import render
import requests
import json

# Create your views here.
def home(request):
    r = requests.get('https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=274a21cd349541feaf3c46da3d50db0e')
    
    api = json.loads(r.content)
    return render(request,'getNews/home.html',{'api':api})
