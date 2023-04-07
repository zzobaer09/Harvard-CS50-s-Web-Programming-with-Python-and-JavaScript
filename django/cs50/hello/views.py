from django.shortcuts import render, HttpResponse

# Create your views here.


def hello(request): return render(request , "r/index.html")
def helloZo(request): return HttpResponse("hello Zobaer!")
def greet(request , name): return render(request , "hello/greet.html" , {"aname": name.upper})