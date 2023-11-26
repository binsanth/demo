from django.db import models

class travel_table(models.Model):
    objects = None
    img=models.ImageField(upload_to='images')
    name=models.CharField(max_length=200)
    disc=models.TextField()

    def __str__(self):
        return self.name

class team(models.Model):
    pic=models.ImageField(upload_to='images')
    na=models.CharField(max_length=200)
    about=models.TextField()

    def __str__(self):
        return self.na