from django.db import models

class About_model(models.Model):
    image = models.ImageField(upload_to='About_model/%Y/%m/%d')
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=255)


    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'

class About_spering(models.Model):
    image = models.ImageField(upload_to='About_spering/%Y/%m/%d')
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=255)
  

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'About_spering'
        verbose_name_plural = 'Abouts_spering'

