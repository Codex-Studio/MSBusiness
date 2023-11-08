from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовок'
    )
    descriptions = models.TextField(
        verbose_name='Описание',
    )
    image = models.ImageField(
        upload_to='Blog'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Наш проект'
        verbose_name_plural = 'Наши проекты'