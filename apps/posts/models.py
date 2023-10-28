from django.db import models

class Main(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    context = models.CharField(
        max_length=50,
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='main/',
        verbose_name='Фотография'
    )
    image2 = models.ImageField(
        upload_to='main/',
        verbose_name='Фотография заднего фона'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Главная строница'

ICON = (
    ("Изучение", "Изучение"),
    ("РАЗРАБОТКА", "РАЗРАБОТКА"),
    ("ЗАПУСК", "ЗАПУСК"),
)

class Job(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    context = models.CharField(
        max_length=255,
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='job/',
        verbose_name='Фотография'
    )
    image_title = models.CharField(
        max_length=155,
        verbose_name='Заголовка блога'
    )
    image_context = models.CharField(
        max_length=255,
        verbose_name='Описание блога'
    )
    icon = models.CharField(
        choices=ICON,
        max_length=20,
        verbose_name='Выберите иконку' 
    )
    num = models.CharField(
        max_length=20,
        verbose_name='Номер блога'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Настройка Блога'

class About(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовка'
    )
    context = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='about/main',
        verbose_name='Фотография переденго фона'
    )
    image2 = models.ImageField(
        upload_to='about/',
        verbose_name='Фотография заднего фона'
    )
    text = models.TextField(
        verbose_name='Текст'
    )
    end_about = models.CharField(
        max_length=50,
        verbose_name='Читать далее'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'О нас'


class Directions(models.Model):
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
    blog_context = models.TextField(
        verbose_name='Описание Блога'
    )
    end_blog = models.CharField(
        max_length=50,
        verbose_name='Конец Блога'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Натсройка Напрвление'

class Advantages(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    context = models.CharField(
        max_length=155,
        verbose_name='Описание'
    )
    text = models.TextField(
        verbose_name='Текст'
    )
    image = models.ImageField(
        upload_to='advantages/',
        verbose_name='Фото'
    )
    image2 = models.ImageField(
        upload_to='advantages/',
        verbose_name='Фото 2'
    )
    informations_title = models.CharField(
        max_length=155,
        verbose_name='Заголовка Блога'
    )
    informations_context = models.TextField(
        verbose_name='Описание Блога'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Наши преимушество'

ICON_BLOG = (
    ("Довольных клиентов", "Довольных клиентов"),
    ("Опытных сотрудников", "Опытных сотрудников"),
    ("Удовлетворенности", "Удовлетворенности"),
    ("Наград", "Наград"),

)

class Description(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    context = models.CharField(
        max_length=50,
        verbose_name='Процент'
    )
    image = models.ImageField(
        upload_to='description/'
    )
    icon = models.CharField(
        choices=ICON_BLOG,
        max_length=50,
        verbose_name='Выберите иконку'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Описание'

class Application(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    context = models.CharField(
        max_length=155,
        verbose_name='Описание'
    )
    speakers = models.CharField(
        max_length=50,
        verbose_name='Заголовок калонки'
    )
    image = models.ImageField(
        upload_to='speakers/',
        verbose_name='Фото'
    )
    frist_name = models.CharField(
        max_length=100,
        verbose_name='ФИО'
    )
    phone_number = models.CharField(
        max_length=50,
        verbose_name='Номер телефона'
    )
    addres_email = models.CharField(
        max_length=100,
        verbose_name='Google Аккаунт'
    )
    limit = models.CharField(
        max_length=100,
        verbose_name='Лимит бюджета'
    )
    meaning_main = models.CharField(
        max_length=100,
        verbose_name='Значение'
    )
    meaning = models.CharField(
        max_length=155,
        verbose_name='Процент значени'
    )
    end_application = models.CharField(
        max_length=50,
        verbose_name='Конец заявки'
    )
    image2 = models.ImageField(
        upload_to='application/',
        verbose_name='Фотография - 2'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Наши Заявки'

class Klient(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    context = models.CharField(
        max_length=255,
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='klient/',
        verbose_name='Фото'
    )
    end_coment = models.CharField(
        max_length=100,
        verbose_name='Смотреть проекты'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Наши клиенты'