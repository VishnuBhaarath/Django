from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

# Create your views here.
def index(request):
    dest1=Destination()
    dest1.name="Hyderabad"
    dest1.desc="most beautiful city"
    return render(request, "index.html",{'dest1': dest1})
