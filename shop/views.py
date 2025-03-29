from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.

# class Index(ListView):
#     template_name = "shop/index.html"

def index(request):
    return render(request, "shop/index.html")