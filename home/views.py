from django.shortcuts import render, redirect
from .models import Todo
from .forms import CreateRecordForm, UpdateRecordForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def home_page(request) :
    all_records = Todo.objects.all()
    return render(request, 'home.html', {'records' : all_records})

@login_required
def say_hello(request) :
    return render(request, "hello.html")

@login_required
def detail(request, record_id) :
    record = Todo.objects.get(id=record_id)
    return render(request, "detail.html", {"r":record})

@login_required
def delete(request, record_id) :
    Todo.objects.get(id=record_id).delete()
    messages.success(request, 'Record deleted successfully.', extra_tags="success")
    return redirect("homepage")

@login_required
def create(request) :
    if request.method == "POST":
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Todo.objects.create(
                title=cd["title"], 
                body=cd["body"]
                )
            messages.success(request, "Todo added successfully", extra_tags="success")
            return redirect ("homepage")
        
    else :
        form = CreateRecordForm()
    return render(request, "create.html", {"form":form})

@login_required
def update(request, record_id) :
    record = Todo.objects.get(id = record_id)
    if request.method == "POST":
        form = UpdateRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, "Todo updated successfully", extra_tags="success")
            return redirect ("detailtodo", record_id)
    else:
        form = UpdateRecordForm(instance=record)
    return render(request, "update.html", {"form":form})
    