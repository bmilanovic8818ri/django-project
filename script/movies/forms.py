from django.forms import ModelForm
from .models import Movie, Comment


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ('Title', )