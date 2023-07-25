from django.shortcuts import render

# Create your views here.

def temfirst(request):
    return render(request,'temfirst.html')

def temsecond(request):
    return render(request,'temsecond.html')