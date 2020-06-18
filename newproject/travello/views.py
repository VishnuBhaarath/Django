from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
from .models import projects

# Create your views here.
def index(request):
   
    dest1=Destination()
    dest1.name="Aakash Raja"
    dest1.desc="President"
    dest1.img="male2.jpg"
    dest1.price=700

    dest2=Destination()
    dest2.name="Saran"
    dest2.desc="Treasurer"
    dest2.img="male2.jpg"
    dest2.price=600

    dest3=Destination()
    dest3.name="Kumaresh"
    dest3.desc="Vice president"
    dest3.img="male2.jpg"
    dest3.price=600

    dest4=Destination()
    dest4.name="GDK"
    dest4.desc="Vice president"
    dest4.img="male2.jpg"
    dest4.price=600

    dest5=Destination()
    dest5.name="Vishnu"
    dest5.desc="Treasurer"
    dest5.img="male2.jpg"
    dest5.price=600

    dest6=Destination()
    dest6.name="Sn"
    dest6.desc="Treasurer"
    dest6.img="male2.jpg"
    dest6.price=600

    dest7=Destination()
    dest7.name="Sn"
    dest7.desc="Treasurer"
    dest7.img="male2.jpg"
    dest7.price=600

    dest8=Destination()
    dest8.name="an"
    dest8.desc="Treasurer"
    dest8.img="male2.jpg"
    dest8.price=600


    dest10=Destination()
    dest10.name="Sn"
    dest10.desc="Treasurer"
    dest10.img="male2.jpg"
    dest10.price=600

    dest11=Destination()
    dest11.name="an"
    dest11.desc="Treasurer"
    dest11.img="male2.jpg"
    dest11.price=600

    dest12=Destination()
    dest12.name="Sn"
    dest12.desc="Treasurer"
    dest12.img="male2.jpg"
    dest12.price=600

    dest13=Destination()
    dest13.name="Sn"
    dest13.desc="Treasurer"
    dest13.img="male2.jpg"
    dest13.price=600

    dest14=Destination()
    dest14.name="Sn"
    dest14.desc="Treasurer"
    dest14.img="male2.jpg"
    dest14.price=600

    dest15=Destination()
    dest15.name="Sn"
    dest15.desc="Treasurer"
    dest15.img="male2.jpg"
    dest15.price=600
    
    dest16=Destination()
    dest16.name="Sn"
    dest16.desc="Treasurer"
    dest16.img="male2.jpg"
    dest16.price=600
    
    dest17=Destination()
    dest17.name="Sn"
    dest17.desc="Treasurer"
    dest17.img="male2.jpg"
    dest17.price=600
    
    dest18=Destination()
    dest18.name="Rakesh"
    dest18.desc="Member"
    dest18.img="male2.jpg"
    dest18.price=600
    
    dest19=Destination()
    dest19.name="Naveen"
    dest19.desc="Member"
    dest19.img="male2.jpg"
    dest19.price=600
    
    dest20=Destination()
    dest20.name="Lingesh"
    dest20.desc="Member"
    dest20.img="male2.jpg"
    dest20.price=600
    
    dest21=Destination()
    dest21.name="Vishnu"
    dest21.desc="Member"
    dest21.img="male2.jpg"
    dest21.price=600

    
    dests=[dest1,dest2,dest3,dest4,dest5,dest6,dest7,dest8,dest10,dest11,dest12,dest13,dest14,dest15,dest16,dest17,dest18,dest19,dest20,dest21]
    

    return render(request, "index.html",{'dests': dests})
def project(request):
    pro1=projects()
    pro1.name="Aakash Raja"
    pro1.desc="President"
    pro1.img="male2.jpg"
    pro1.price=700

    pro2=projects()
    pro2.name="Aakash Raja"
    pro2.desc="President"
    pro2.img="male2.jpg"
    pro2.price=700

    pros=[pro1,pro2]
    return render(request,"projects.html", {'pros': pros})