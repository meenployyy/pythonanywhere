from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Contact(models.Model):
    fullname = models.CharField(max_length=150)
    time = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=150)
    desc = models.TextField(max_length=250)

    def __str__(self):
        return f'{self.fullname} - {self.time}'


class Province(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Cafe(models.Model):
    name = models.CharField(max_length=150)
    province = models.ForeignKey(Province, on_delete=CASCADE)
    img = models.ImageField(upload_to='uploads/cafe/')
    address = models.TextField(max_length=250)
    desc = models.TextField(max_length=250)

    def __str__(self):
        return self.name