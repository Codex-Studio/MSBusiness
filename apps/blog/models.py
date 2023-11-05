from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    description = models.CharField(
        max_length=155,
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='blog',
        verbose_name='Фото'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Блог'


class OurProjects(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    descriptio1 = models.CharField(
        max_length=255,
        verbose_name='Номер колонки - 1', 
        blank=True, null=True
    )
    descriptio2 = models.CharField(
        max_length=255,
        verbose_name='Номер колонки - 2',
        blank=True, null=True
    )
    descriptio3 = models.CharField(
        max_length=255,
        verbose_name='Номер колонки - 3',
        blank=True, null=True
    )
    descriptio4 = models.CharField(
        max_length=255,
        verbose_name='Номер колонки - 4',
        blank=True, null=True
    )
    image = models.ImageField(
        upload_to='project',
        verbose_name='фото'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Наши проекты'