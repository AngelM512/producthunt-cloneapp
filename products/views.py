from django.shortcuts import render

# Create your views here.

def homepage(request):
    content = {}
    return render(request, 'products/index.html')