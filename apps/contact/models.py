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
        upload_to='contect/',
        verbose_name='Фото'
    )
    end_main = models.CharField(
        max_length=155,
        verbose_name='Конец'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Контакты'

class Contact(models.Model):
    image = models.ImageField(
        upload_to='contact/contact',
        verbose_name='Фото'
    )
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    context = models.CharField(
        max_length=155,
        verbose_name='Описание'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Наши контакты'

class ContactAs(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    context = models.CharField(
        max_length=155,
        verbose_name='Описание'
    )
    end_contact = models.CharField(
        max_length=155,
        verbose_name='Конец'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Связаться'