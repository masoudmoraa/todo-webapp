from django.shortcuts import render, redirect
from .models import Todo

def home_page(request) :
    all_records = Todo.objects.all()
    return render(request, 'home.html', {'records' : all_records})


def say_hello(request) :
    return render(request, "hello.html")


def detail(request, record_id) :
    record = Todo.objects.get(id=record_id)
    return render(request, "detail.html", {"r":record})

def delete(request, record_id) :
    Todo.objects.get(id=record_id).delete()
    return redirect("homepage")