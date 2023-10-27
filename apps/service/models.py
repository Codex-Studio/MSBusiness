from django.db import models

# Create your models here.
class Main(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    context = models.CharField(
        max_length=300,
        verbose_name="Описание"
    )
    title1 = models.CharField(
        max_length=155,
        verbose_name='Главная'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Заголовка Услуги'

class Services(models.Model):
    image = models.ImageField(
        upload_to='service/',
        verbose_name='Фотография'
    )
    image_title = models.CharField(
        max_length=100,
        verbose_name='Заголовка фотографий'
    )
    image_context = models.TextField(
        verbose_name='Описание фотографий'
    )
    end_image = models.CharField(
        max_length=100,
        verbose_name='Конец фотографий'
    )
    number = models.CharField(
        max_length=20,
        verbose_name='Номер Блога'
    )

    def __str__(self):
        return self.image_title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Настройки Блога'

class ServiceTitle(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Заголовка'
    )
    context = models.TextField(
        verbose_name='Описание'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Заголовка Блога'
