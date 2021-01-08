from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=30)
    rented = models.BooleanField(default=False)
    rented_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    description = models.TextField(max_length=400, null=True)
    user = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.title
