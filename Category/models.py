from django.db import models

class Category_model(models.Model):
    image = models.ImageField(upload_to='Category_model/%Y/%m/%d')
    title = models.CharField(max_length=100)


    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category sections'