from django.db import models

# Define dymanic information and store it in our database.


class Blog (models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()
    slug = models.SlugField(unique=True)
