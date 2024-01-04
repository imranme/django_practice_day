from django.shortcuts import render,redirect
from . import forms

from . import models
# Create your views here.


def add_musician(request):
    musician_form=forms.MusicianForm(request.POST)
    if request.method=='POST':
        if musician_form.is_valid():
            musician_form.save()
            return redirect('add_musician')
    else:
        musician_form=forms.MusicianForm()

    return render(request,'Musician/add_musician.html',{'form':musician_form})

def edit_musician(request,id):
    musician_id=models.musician.objects.get(pk=id)
    musician_instance=forms.MusicianForm(instance=musician_id)
    if request.method=='POST':
        musician_instance=forms.MusicianForm(request.POST,instance=musician_id)
        if musician_instance.is_valid():
            musician_instance.save()
            return redirect('home')
    
    return render(request,'musician/add_musician.html',{'form':musician_instance})
