from django.shortcuts import render,redirect 
from album.models import album

def home(request):
    data=album.objects.all()
    print(data)
    return render(request, 'home.html',{'data':data})