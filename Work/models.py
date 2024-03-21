from django.db import models

class Work_model(models.Model):
    image = models.ImageField(upload_to='Work/%Y/%m/%d')
    cost = models.CharField(max_length=50)
    title = models.CharField(max_length=100)


    def __str__(self) -> str:
        return self.title
    

    class Meta:
        verbose_name = 'Work'
        verbose_name_plural = 'Works'