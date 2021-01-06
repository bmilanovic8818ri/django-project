from django.forms import ModelForm
from .models import Movie, Comment


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'rented', 'rented_count', 'created_at', 'updated_at')


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('content', 'created_at', 'updated_at', 'movie')
