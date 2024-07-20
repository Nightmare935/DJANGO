from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    name = "Himanshu"
    data = {'name':'nice'}
    
    
    
    return render(request,'home.html',data)

def first(request):
    return render(request,'first.html')

def second(request):
    return render(request,'second.html')