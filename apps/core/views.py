from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def diagnostic(request):
    return render(request, "diagnostic.html")

def expert(request):
    return render(request, "expertIA.html")

def about(request):
    return render(request, "apropos.html")

def community(request):
    return render(request, "community.html")