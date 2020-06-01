from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bhivemembers(request):
    return render(request, 'bhivemembers.html')

# Create your views here.
