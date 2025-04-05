from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.contrib.auth import logout, authenticate, login
from shop.forms import SignInForm, SignUpForm

# Create your views here.

# class Index(ListView):
#     template_name = "shop/index.html"

def index(request):
    return render(request, "shop/index.html")

def signup(request):
    form = SignUpForm(data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password1")
            user = authenticate(request, username=email, password=password)
            if user:
                login(request,user)
                return redirect("index")
    context = {
        "title":"Sign Up",
        "form":form
    }
    return render(request, "shop/signup.html", context)

def signin(request):
    form = SignInForm(data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            email = request.POST.get("email")
            password = request.POST.get("password")
            user = authenticate(request, username=email, password=password)
            if user:
                login(request,user)
                return redirect("index")
    context = {
        "title":"Sign In",
        "form":form
    }
    return render(request, "shop/signin.html", context)

def signout(request):
    logout(request)
    return redirect("signin")



