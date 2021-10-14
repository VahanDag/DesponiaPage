from django.db import models

# Create your models here.

class Category(models.Model):
    categoryName = models.CharField(max_length=100, verbose_name="Category Name")
    categoryBrand = models.CharField(max_length=100, verbose_name="Category Brand")
    Categorydescription = models.TextField(verbose_name="Description")
    totalPost = models.IntegerField(verbose_name="Total Post",null=True,blank=True,default=0)
    totalMessage = models.IntegerField(verbose_name="Total Message",null=True,blank=True,default=0)


    def __str__(self):
        return self.categoryName
