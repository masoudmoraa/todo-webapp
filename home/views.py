from django.shortcuts import render
from .models import Todo

def home_page(request) :
    all_records = Todo.objects.all()
    return render(request, 'home.html', {'records' : all_records})


def say_hello(request) :
    return render(request, "hello.html")