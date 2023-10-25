from django.db import models

# Create your models here.
class Post(models.Model):
    title1 = models.CharField(
        max_length=155,
        verbose_name="Заголвка - 1"
    )
    image_main = models.ImageField(
        upload_to='main',
        verbose_name='Фото большое'
    )
    image = models.ImageField(
        upload_to='galerry',
        verbose_name='Фото маленький'
    )
    context = models.CharField(
        max_length=100,
        verbose_name="Описание"
    )

    def __str__(self):
        return self.title1
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Настройка глвной строницы'

class Jobs(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name="Заголовка"
    )
    context = models.CharField(
        max_length=355,
        verbose_name="Описание"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Заголовка Работы '

ICON = (
    ("Разработка" , "Разработка"),
    ("Изучение" , "Изучение"),
    ("Запуск" , "Запуск")
)

class Job(models.Model):
    image = models.ImageField(
        upload_to='job',
        verbose_name='Фотография работы'
    )
    icon = models.CharField(
        choices= ICON,
        max_length=155,
        verbose_name="Выберите иконку"
    )
    image_title = models.CharField(
        max_length=100,
        verbose_name='Заголвка фотографий'
    )
    image_context = models.CharField(
        max_length=300,
        verbose_name='Описание фотографий'
    )
    number = models.CharField(
        max_length=1,
        verbose_name='Номер работы'
    )

    def __str__(self):
        return self.image_title
    

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Настройки работы'

class Main_About(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Заголовка О нас'
    )
    context = models.CharField(
        max_length=155,
        verbose_name='Описание о нас'
    )
    text = models.TextField(
        verbose_name='Текст'
    )
    image_main = models.ImageField(
        upload_to='about',
        verbose_name='Фото'
    )
    endabout = models.CharField(
        max_length=55,
        verbose_name='конец'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'О Нас'

class Min_About(models.Model):
    title = models.CharField(
        max_length=1,
        verbose_name='QWERTYU'
    )
    image = models.ImageField(
        upload_to='about/main',
        verbose_name='Задний фотография'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Задний фотография'

class Direction_Main(models.Model):
    title_main = models.CharField(
        max_length=50,
        verbose_name='Заголовка'
    )
    context_main = models.CharField(
        max_length=100,
        verbose_name='Описание'
    )
    def __str__(self):
        return self.title_main
    
    class meta:
        verbose_name = ''
        verbose_name_plural = 'Настройки Главной Направление'

class Direction(models.Model):
    title = models.CharField(
        max_length=155, 
        verbose_name='Заголовка Блога'
    )
    context = models.CharField(
        max_length=300,
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
        verbose_name_plural = 'Настройки Направление'

class Advantages(models.Model):
    more_details1 = models.CharField(
        max_length=155,
        verbose_name='Загаловка - 1'
    )
    more_details_text1 = models.TextField(
        verbose_name='Описание - 1'
    )
    def __str__(self):
        return self.more_details1
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Наши Преимущества'

class Advantage(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Заголовка'
    )
    context = models.CharField(
        max_length=255,
        verbose_name='Описание'
    )
    text = models.TextField(
        verbose_name='Текст'
    )
    more_details1 = models.CharField(
        max_length=155,
        verbose_name='Загаловка - 1'
    )
    more_details_text1 = models.TextField(
        verbose_name='Описание - 1'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Настройка  Наши Преимущество' 

class ImageAdvantage(models.Model):
    image = models.ImageField(
        upload_to='advantage/',
        verbose_name='Фото'
    )
    title = models.CharField(
        max_length=1,
        verbose_name='заголовка'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Фотография Преимущество'

ICON_STATUS = (
    ('Довольных Клиенты', 'Довольных Клиенты'),
    ('Опытных сотрудников', 'Опытных сотрудников'),
    ('Удовлетворенности', 'Удовлетворенности'),
    ('Наград', 'Наград')
)

class Status(models.Model):
    grade = models.CharField(
        max_length=50, 
        verbose_name='Отценка'
    )
    context1 = models.CharField(
        max_length=100,
        verbose_name='Довольных Клиенты'
    )
    status_icon = models.CharField(
        choices=ICON_STATUS,
        max_length=50,
        verbose_name='Выберите иконку'
    )

    def __str__(self):
        return self.grade
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Настройки Процентов Клиентов'

class Application(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    context = models.CharField(
        max_length=155,
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to=True,
        verbose_name='Фото справа'
    )
    image2 = models.ImageField(
        upload_to=True,
        verbose_name='Фото слева'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Заголовка Заявки'

class Applications(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Заголовка'
    )
    fio = models.CharField(
        max_length=100,
        verbose_name="ФИО"
    )
    phone = models.CharField(
        max_length=30,
        verbose_name='Номер телефона'
    )
    addres = models.CharField(
        max_length=100,
        verbose_name='Адресс'
    )
    limit = models.CharField(
        max_length=155,
        verbose_name='Лимит'
    )
    choise = models.CharField(
        max_length=155,
        verbose_name='Выбор значение'
    )
    percent = models.CharField(
        max_length=100,
        verbose_name='Процент'
    )
    end = models.CharField(
        max_length=50,
        verbose_name='Отправка'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Настройка Заявки'

class Applicati(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Заголовка'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Заголовка Отделов' 

class Clients(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    context = models.CharField(
        max_length=300,
        verbose_name='Описание'
    )
    end = models.CharField(
        max_length=100,
        verbose_name='Конец'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Наши Клиенты'


class Client(models.Model):
    image = models.ImageField(
        upload_to='clients/',
        verbose_name='Фото'
    )
    title = models.CharField(
        max_length=100,
        verbose_name='Не важно'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Фотография Клиентов'


class Footer(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Заголовка - 1'
    )
    title2 = models.CharField(
        max_length=150,
        verbose_name='Заголовок - 2'
    )
    title3 = models.CharField(
        max_length=150,
        verbose_name='Заголовок - 3'
    )

    def __srt__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Услуги'

class Foote(models.Model):
    context = models.CharField(
        max_length=255,
        verbose_name='Подзаголовок 1 Услуги'
    ) 
    context2 = models.CharField(
        max_length=255,
        verbose_name='Подзаголовок 2 Услуги'
    )
    photo = models.ImageField(
        upload_to='photos/',
        verbose_name='Фото'
    )

    def __str__(self):
        return self.context
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Подзаголовок Услуги'

