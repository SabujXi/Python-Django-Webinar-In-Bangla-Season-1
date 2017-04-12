from django.shortcuts import render

from django.http import HttpResponse

def hi(request):
    return HttpResponse("You said hi I said bye")

def index(r):
    return render(r, "sunflower/index.html")
