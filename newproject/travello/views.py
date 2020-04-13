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
    dest1.img='destination_1.jpg'

    dest2=Destination()
    dest2.name="Mumbai"
    dest2.desc="most expensive city"
    dest2.img='destination_2.jpg'

    dests = [dest1, dest2]
    return render(request, "index.html",{'dests': dests})
