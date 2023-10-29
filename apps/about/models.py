from django.db import models

# Create your models here.
class About(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    context = models.CharField(
        max_length=155,
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='about/',
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
        verbose_name_plural = 'О нас'
        
class Companion(models.Model):
    blog_title = models.CharField(
        max_length=100,
        verbose_name='Заголовка Блога'
    )
    blog_context = models.CharField(
        max_length=100,
        verbose_name='Описание Блога'
    )
    title = models.CharField(
        max_length=100,
        verbose_name='ЗАголовка'
    )
    text1 = models.TextField(
        verbose_name='Текс'
    )
    text2 = models.TextField(
        verbose_name='Текст - 2'
    )
    image = models.ImageField(
        upload_to='companion/',
        verbose_name='Фото'
    )


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Наша компания'

# class Insurance(models.Model):

class Develop(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    context = models.CharField(
        max_length=255,
        verbose_name='Описание'
    )
    text = models.TextField(
        verbose_name='Текст'
    )
    image = models.ImageField(
        upload_to='develop',
        verbose_name='Фото'
    )
    video = models.CharField(
        max_length=155,
        verbose_name='Видео'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name =''
        verbose_name_plural ='Почему Выбрали нас'

ICON = (
    ('Довольных клиентов', 'Довольных клиентов'),
    ('Опытных сотрудников', 'Опытных сотрудников'),
    ('Уровень удовлетворенности', 'Уровень удовлетворенности'),
    ('Многолетний опыт', 'Многолетний опыт'),
    ('Награды', 'Награды')
)

class Achievement(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовака'
    )
    context = models.CharField(
        max_length=155,
        verbose_name='Описание'
    )
    icon = models.CharField(
        choices=ICON,
        max_length=155,
        verbose_name='Выберите иконку'
    )
    title_icon = models.CharField(
        max_length=155,
        verbose_name='Процент'
    )
    context_icon = models.CharField(
        max_length=155,
        verbose_name='Описание'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Наши Достижение'

class Comand(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    context = models.CharField(
        max_length=155,
        verbose_name='Описание'
    )
    image = models.ImageField(
        max_length=155,
        verbose_name='Фото'
    )
    title_image = models.CharField(
        max_length=155,
        verbose_name='Заголовка Фото'
    )
    context_image = models.CharField(
        max_length=155,
        verbose_name='Описание Фото'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name = 'Наша Команда'

class Klient(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    context = models.CharField(
        max_length=155,
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='klient/',
        verbose_name='Фото'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Наши клиенты'

class Requests(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    blog_title = models.CharField(
        max_length=155,
        verbose_name='Заголовка Блога'
    )
    image_blog = models.ImageField(
        upload_to='requests/',
        verbose_name='Фото'
    )
    context_blog = models.CharField(
        max_length=155,
        verbose_name='Описание Блога'
    )
    blog_text = models.TextField(
        verbose_name='Текст'
    )
    end_blog = models.CharField(
        max_length=100,
        verbose_name='ОТЗЫВ'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Часто Задаваемые Вопросы'
        
