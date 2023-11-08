from django.db import models
from django_resized.forms import ResizedImageField


# Create your models here.
class Service(models.Model):
    title = models.CharField(
        max_length=127,
        verbose_name='Название'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = ResizedImageField(
        force_format="WEBP",
        quality=100,
        upload_to='teacher_img/',
        verbose_name="Фотография услуги",
        blank = True, null = True
    )

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

