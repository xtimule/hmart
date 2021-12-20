from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='photo/category' , blank=True)
    slug = models.SlugField(max_length=50, unique=True)
    def __str__(self):
        return self.name


# Create your models here.
