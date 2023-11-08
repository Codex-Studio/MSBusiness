from django.db import models

# Create your models here.
class About(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Описание'
    )
    text = models.TextField(
        verbose_name='Текст'
    )
    context = models.TextField(
        verbose_name='Текст 2'
    )
    image = models.ImageField(
        upload_to='about',
        verbose_name='Фото'
    )
    business_title = models.CharField(
        max_length=155,
        verbose_name='Заголовка Бизнеса'
    )
    business_context = models.TextField(
        verbose_name='Текст Бизнеса'
    )
    image = models.ImageField(
        upload_to='businee',
        verbose_name='Фото'
    )
    video = models.URLField(
        verbose_name='Видео'
    )
    title_team = models.CharField(
        max_length=155,
        verbose_name='Заголовка Команды'
    )
    request_title = models.CharField(
        max_length=155,
        verbose_name='Заголовка Запросов'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Настройки Всего О нас'

class Team(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Зголовка'
    )
    context = models.CharField(
        max_length=100,
        verbose_name='Должность'
    )
    image = models.ImageField(
        upload_to='team/',
        verbose_name='Фото'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Наша Команда'

class Review(models.Model):
    name = models.CharField(
        max_length=155,
        verbose_name='ФИО'
    )
    context = models.CharField(
        max_length=155,
        verbose_name='Должность'
    )
    image = models.ImageField(
        upload_to='review',
        verbose_name='Фото'
    )
    review = models.CharField(
        max_length=300,
        verbose_name='Отзывы'
    )
    review_name = models.CharField(
        max_length=155,
        verbose_name='Отзыв От '
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Отзывы'
