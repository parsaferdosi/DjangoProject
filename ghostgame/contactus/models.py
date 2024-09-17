from django.db import models

# Create your models here.
class ticket(models.Model):
    firstname=models.CharField(max_length=16)
    lastname=models.CharField(max_length=50)
    email=models.EmailField(max_length=256)
    subject=models.CharField(max_length=16)
    message=models.TextField()
    timecreate=models.DateField(auto_now_add=True)