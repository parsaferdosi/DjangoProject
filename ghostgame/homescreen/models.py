from django.db import models
from django.utils.text import slugify
# Create your models here.

class gamegenre(models.Model):
    title=models.CharField(max_length=16)
    slug=models.SlugField(default='',null=False,db_index=True)
    def save(self,*args,**kwargs):
        self.slug=slugify(str({self.title}))
        super().save(*args,**kwargs)
    def __str__(self) -> str:
        return f'{self.title}'
class suggestion(models.Model):
    gamename=models.CharField(max_length=50)
    discription=models.TextField()
    discription2=models.TextField(null=False,blank=True)
    slug=models.SlugField()
    genre=models.ForeignKey(gamegenre,on_delete=models.CASCADE,null=True,blank=True,related_name='category')
    suggestion=models.BooleanField(default=False)
    gameImage=models.ImageField(null=False,blank=True,upload_to='homescreen')
    def save(self,*args,**kwargs):
        self.slug=slugify(str({self.gamename}))
        super().save(*args,**kwargs)
    def __str__(self) -> str:
        return f'{self.gamename}'
