from django.db import models

# Create your models here.
class Main(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    context = models.CharField(
        max_length=255,
        verbose_name='описание'
    )
    image = models.ImageField(
        upload_to='team',
        verbose_name='Фото'
    )
    end = models.CharField(
        max_length=155,
        verbose_name='Конец'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Команда'

class Team(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    context = models.CharField(
        max_length=255,
        verbose_name='Описание'
    )
    blog_title = models.CharField(
        max_length=155,
        verbose_name='Заголовка Блога'
    )
    blog_context = models.CharField(
        max_length=255,
        verbose_name='Описание Блога'
    )
    image_blog = models.ImageField(
        upload_to='team-details',
        verbose_name='Фото Блога'
    )
    blog_title2 = models.CharField(
        max_length=155,
        verbose_name='Заголовка Блога - 2'
    )
    blog_context2 = models.CharField(
        max_length=255,
        verbose_name='Описание Блога - 2'
    )
    image_blog2 = models.ImageField(
        upload_to='team-details',
        verbose_name='Фото Блога - 2'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Блога Нашей команды'

