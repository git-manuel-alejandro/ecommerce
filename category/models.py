from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=70 , unique= True)
    description = models.CharField(max_length=256 , blank=True)
    slug = models.CharField(max_length=100 , unique= True)
    cat_imagen = models.ImageField(upload_to='photos/categories' , blank = True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name