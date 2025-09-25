from django.urls import path
from . import views

urlpatterns = [
    # path(url, view),
    path('', views.home_page, name="homepage"),
    path('hello/', views.say_hello, name="hellopage"),
    path('detail/<int:record_id>', views.detail, name="detailpage"),
    path('delete/<int:record_id>', views.delete, name="deletetodo"),
    path('create/', views.create, name="createtodo")
]
