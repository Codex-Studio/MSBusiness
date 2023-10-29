from django.db import models

# Create your models here.
class Main(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    context = models.CharField(
        max_length=155,
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='blog/',
        verbose_name='Фото'
    )
    end_blog = models.CharField(
        max_length=100,
        verbose_name='Конец'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Настройки Блога'

class Projects(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    text1 = models.TextField(
        verbose_name='Подзаголовок - 1'
    )
    text2 = models.TextField(
        verbose_name='Подзаголовок - 2'
    )
    text3 = models.TextField(
        verbose_name='Подзаголовок - 3'
    )
    text4 = models.TextField(
        verbose_name='Подзаголовок - 4'
    )
    image = models.ImageField(
        upload_to='projects/',
        verbose_name='Фото'
    )
    end_projectrs = models.CharField(
        max_length=155,
        verbose_name='Конец'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Наши проекты'
