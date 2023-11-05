from django.db import models

# Create your models here.
class About(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    description = models.CharField(
        max_length=255,
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='about/',
        verbose_name='Фото'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Настройки Всего О нас'

class Companion(models.Model):
    description = models.TextField(
        verbose_name='Текст'
    )
    descriptions = models.TextField(
        verbose_name='Текст - 2'
    )
    image = models.ImageField(
        upload_to='companion',
        verbose_name='Фото'
    )

    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'О компаний'

class Business(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    descriptions = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='business',
        verbose_name='Фото'
    )
    video = models.URLField(
        verbose_name='Видео'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Бизнес'

class Team(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='ФИО'
    )
    descriptions = models.CharField(
        max_length=255,
        verbose_name='Должность'
    )
    image = models.ImageField(
        upload_to='team',
        verbose_name='Фото'
    )
    review = models.TextField(
        verbose_name='Отзывы'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Наша команда'