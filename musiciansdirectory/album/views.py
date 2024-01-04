from django.shortcuts import render,redirect
from . import forms 

from . import models 

# Create your views here.

def add_album(request):

    album_form=forms.AlbumForm(request.POST)
    if request.method == 'POST':
        if album_form.is_valid():
            print(album_form)
            album_form.save()
            return redirect('add_album')
    else:
        album_form=forms.AlbumForm()

    return render(request, 'album/add_album.html',{'form':album_form})

def edit_album(request,id):

    album_id=models.album.objects.get(pk=id)
    album_instance=forms.AlbumForm(instance=album_id)
    if request.method=='POST':
        album_instance=forms.AlbumForm(request.POST,instance=album_id)
        if album_instance.is_valid():
            album_instance.save()
            return redirect('add_album')
    return render(request, 'Album/add_album.html',{'form':album_instance})

def delete_album(request,id):
    album_id=models.album.objects.get(pk=id)
    album_id.delete()
    return redirect('home')


