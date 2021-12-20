from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='photo/category' , blank=True)
    def __str__(self):
        return self.name


# Create your models here.
