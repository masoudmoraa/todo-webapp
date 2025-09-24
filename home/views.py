from django.shortcuts import render


def home_page(request) :
    return render(request, 'home.html')


def say_hello(request) :
    return render(request, "hello.html")