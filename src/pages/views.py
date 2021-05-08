from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
  my_context = {
    "my_text": "This is about me"
  }
  return render(request, "home.html", my_context)

def contact_view(request, *args, **kwargs):
  return HttpResponse("<h1>Contact Page</h1>")

def about_view(request, *args, **kwargs):
  return HttpResponse("<h1>About Page</h1>")

def social_view(request, *args, **kwargs):
  return HttpResponse("<h1>Social Page</h1>")