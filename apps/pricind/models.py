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
        upload_to='pricind/',
        verbose_name='Фото'
    )
    end = models.CharField(
        max_length=155,
        verbose_name='Конец'
    )

    def __Str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'ценообразование'

class Escort(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    title_blog = models.CharField(
        max_length=155,
        verbose_name='Заголовка Блога'
    )
    context_blog = models.CharField(
        max_length=300,
        verbose_name='Описание Блога'
    )
    end_blog = models.CharField(
        max_length=100,
        verbose_name=' Конец Блога'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Сопровождение Бизнеса'

class  Questions(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    context = models.CharField(
        max_length=255,
        verbose_name='Описание'
    )
    context_title = models.CharField(
        max_length=255,
        verbose_name='Заголовка описание'
    )
    blogtitle = models.CharField(
        max_length=155,
        verbose_name='Заголовка Блога'
    )
    blogcontext = models.TextField(
        verbose_name='Описание Блога'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Часто Задаваемые вопросы'
        verbose_name_plural = 'Часто Задаваемые вопросы'

class Questions2(models.Model):
    blog_title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    blog_context = models.TextField(
        verbose_name='Описание'
    )

    def __str__(self):
        return self.blog_title
    
    class Meta:
        verbose_name =''
        verbose_name_plural ='Часто Задаваемые вопросы 2 Блог'
