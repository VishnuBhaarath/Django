from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html',{'name':'sibi'})
def add(request):
    val1=4
    val2=3
    res=val1+val2
    return render(request,'result.html',{'result':res})