from django.db import models

# Create your models here.
class Post(models.Model):
    title1 = models.CharField(
        max_length=155,
        verbose_name="Заголвка - 1"
    )
    image_main = models.ImageField(
        upload_to='main',
        verbose_name='Фото большое'
    )
    image = models.ImageField(
        upload_to='galerry',
        verbose_name='Фото маленький'
    )
    context = models.CharField(
        max_length=100,
        verbose_name="Описание"
    )

    def __str__(self):
        return self.title1
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Настройка глвной строницы'

class Job(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name="Заголовка"
    )
    context = models.CharField(
        max_length=355,
        verbose_name=""
    )