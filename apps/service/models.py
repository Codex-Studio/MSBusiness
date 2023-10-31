from django.db import models

# Create your models here.
class Main(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    context = models.CharField(
        max_length=300,
        verbose_name="Описание"
    )
    title1 = models.CharField(
        max_length=155,
        verbose_name='Главная'
    )
    image = models.ImageField(
        upload_to='service/',
        verbose_name='Фото'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Заголовка Услуги'

class Services(models.Model):
    image = models.ImageField(
        upload_to='service/',
        verbose_name='Фотография'
    )
    image_title = models.CharField(
        max_length=100,
        verbose_name='Заголовка фотографий'
    )
    image_context = models.TextField(
        verbose_name='Описание фотографий'
    )
    end_image = models.CharField(
        max_length=100,
        verbose_name='Конец фотографий'
    )
    number = models.CharField(
        max_length=20,
        verbose_name='Номер Блога'
    )

    def __str__(self):
        return self.image_title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Настройки Блога'

class ServiceTitle(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Заголовка'
    )
    context = models.TextField(
        verbose_name='Описание'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Заголовка Блога'


class ServiceDetails(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    context = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='service_detaild/',
        verbose_name='Фотография'
    )
    end_details_main = models.CharField(
        max_length=100,
        verbose_name='Последняя строка'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Настройка Детального Услуги'

class Team(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Заголовка'
    )
    title2 = models.CharField(
        max_length=100,
        verbose_name='Заголовка - 2'
    )
    text = models.TextField(
        verbose_name='Текст'
    )
    image = models.ImageField(
        upload_to='team/',
        verbose_name='Фотография команды'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Наша команда'

class TeamWide(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Заголовка'
    )
    speakers = models.CharField(
        max_length=255,
        verbose_name='Колонки'
    )
    image = models.ImageField(
        upload_to='teamwide/',
        verbose_name='Фотография'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Широкая География'

ICON = (
    ("Стратегическое Консультирование", "Стратегическое Консультирование"),
    ("Финансовое Планирование", "Финансовое Планирование"),
    ("Достижение Результатов", "Достижение Результатов"),
    ("Поддержка На Всех Этапах", "Поддержка На Всех Этапах"),
)

class Consulting(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Заголовок'
    )
    context = models.CharField(
        max_length=255,
        verbose_name='Описание'
    )
    icon = models.CharField(
        choices=ICON,
        max_length=155,
        verbose_name='Выберите Иконку'
    )
    icon_context = models.CharField(
        max_length=255,
        verbose_name='Заголовка иконки'
    )
    icon_end = models.CharField(
        max_length=100,
        verbose_name='Конец Консалтингов'
    )


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Настройка Консалтингов'

class Business(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    context = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='busines/main',
        verbose_name='Фотография задниго фона'
    )
    title_blog = models.CharField(
        max_length=155,
        verbose_name="Заголовка Блога"
    )
    context_blog = models.CharField(
        max_length=300,
        verbose_name='Описание Блога'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Настройка Бизнеса'