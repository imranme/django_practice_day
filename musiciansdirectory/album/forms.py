from . models import album
from django import forms 

class AlbumForm(forms.ModelForm):

    class Meta:

        model=album
        fields='__all__'

        labels={
            'Name':'Album Name',
            'ReleaseDate':'Release Date',
            'Rating':'Rating',
            'MusicianList':'Musician List',
        }

        help_text ={
            'Rating':'Enter the rating between 1 and 5',
            'ReleaseDate':'Enter the release date',
            'Name':'Enter the name of the album',
        }
        widgets={
            'ReleaseDate':forms.DateInput(attrs={'type':'date'}),
        }