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


#Для детального просмотра блога

class BlogDetails(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    context = models.CharField(
        max_length=155,
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='blogdetails/',
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
        verbose_name_plural = 'Настройки Детального Блога'

class Business(models.Model):
    image = models.ImageField(
        upload_to='business/',
        verbose_name='Фото'
    )
    text = models.TextField(
        verbose_name='текст'
    )
    kolonki1 = models.CharField(
        max_length=155,
        verbose_name='1 Колонка'
    )
    kolonki2 = models.CharField(
        max_length=155,
        verbose_name='2 Колонка'
    )
    kolonki3 = models.CharField(
        max_length=155,
        verbose_name='3 Колонка'
    )
    teg_main = models.CharField(
        max_length=155,
        verbose_name='Заголовка Тегов'
    )
    teg1 = models.CharField(
        max_length=155,
        verbose_name='Теги'
    )


    def __str__(self):
        return self.kolonki1
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Сопровождение Бизнеса'
