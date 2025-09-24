from django.urls import path
from . import views

urlpatterns = [
    # path(url, view),
    path('hello/', views.say_hello),
]
