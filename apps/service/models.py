from django.db import models

class Service(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    context = models.CharField(
        max_length=255,
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='service',
        verbose_name='Фото'
    )
    number_blog = models.CharField(
        max_length=50,
        verbose_name='Номер Блога'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Наши Услуги'
        
