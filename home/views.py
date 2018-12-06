from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(req):
    return render(req,'home/index.html',{})

def about(req):
    return HttpResponse("<h1>Beg ME on</h1>")