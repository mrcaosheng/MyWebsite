from django.shortcuts import render, render_to_response

# Create your views here.

def index(request):
    content = {
        "info": "success"
    }
    return render(
        request, "index.html", content
    )

def login(request):
    content={
        "info": "success"
    }
    return render(request, "main/login.html", content)

def register(request):
    content={
        "info": "success"
    }
    return render(request, "main/register.html", content)